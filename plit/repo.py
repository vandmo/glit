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
        (prefix, repository) = line.split(' ', 1)
        return cls(repository, prefix)

    def clone(self, folder):
        group_folder = os.path.join(folder, self._prefix)
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


class ReposFile():
    def __init__(self, filename):
        self._filename = filename
        self._repositories = [
            Repo.parse(line)
            for line in _read_and_trim(filename)]

    def clone(self, folder):
        for repo in self._repositories:
            repo.clone(folder)


class RepoSet():
    def __init__(self, name, folder, repositories_filename):
        self._reposfile = ReposFile(repositories_filename)
        self._folder = folder

    def clone(self):
        self._reposfile.clone(self._folder)
