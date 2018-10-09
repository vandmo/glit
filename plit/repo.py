from __future__ import print_function

import os
import subprocess
from utils import errordie, msg


def _mkpath(path):
    if not os.path.exists(path):
        os.makedirs(path)


def _trim(lines):
    stripped = [line.strip() for line in lines]
    return [line for line in stripped if line and not line.startswith('#')]


def _read_and_trim(filename):
    with open(filename) as f:
        lines = f.readlines()
    return _trim(lines)


class Repo():
    def __init__(self, repository, prefix):
        self._repository = repository
        self._prefix = prefix

    @classmethod
    def parse(cls, line):
        parts = line.split(' ', 1)
        if len(parts) == 2:
            repository = parts[1]
            prefix = parts[0]
        else:
            errordie('Invalid repository file line: {}'.format(line))
        return cls(repository, prefix)

    def clone(self, folder):
        if self._prefix:
            group_folder = os.path.join(folder, self._prefix)
        else:
            group_folder = folder
        _mkpath(group_folder)
        git_folder = self._repository.rsplit('/', 1)[1]
        if git_folder.endswith('.git'):
            git_folder = git_folder[:-4]
        destination = os.path.join(group_folder, git_folder)
        if os.path.exists(destination):
            msg('IN %s SKIPPING %s' % (self._prefix, git_folder))
            return
        msg('IN %s CLONING %s' % (self._prefix, git_folder))
        args = ['git', 'clone', self._repository, destination]
        status = subprocess.call(args)
        if status:
            errordie('git failed with {}'.format(status))

    def as_line(self):
        if self._prefix:
            return '{} {}'.format(self._prefix, self._repository)
        else:
            return '. {}'.format(self._repository)


class ReposFile():
    def __init__(self, filename):
        self._filename = filename
        self._repositories = [
            Repo.parse(line)
            for line in _read_and_trim(filename)]

    def clone(self, folder):
        for repo in self._repositories:
            repo.clone(folder)

    def add(self, repo):
        self._repositories.append(repo)

    def save(self):
        lines = [repo.as_line()+'\n' for repo in self._repositories]
        with open(self._filename, 'w') as f:
            f.writelines(sorted(lines))


class RepoSet():
    def __init__(self, name, folder, repositories_filename):
        self._name = name
        self._reposfile = ReposFile(repositories_filename)
        self._folder = folder

    def clone(self):
        msg('CLONING SET {}'.format(self._name))
        self._reposfile.clone(self._folder)

    def add_and_clone(self, repository, prefix):
        msg('IN SET {}'.format(self._name))
        repo = Repo(repository=repository, prefix=prefix)
        self._reposfile.add(repo)
        self._reposfile.save()
        repo.clone(self._folder)
