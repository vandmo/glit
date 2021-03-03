from . import git
import os
from .utils import errordie, mkpath, msg


def _trim(lines):
    stripped = [line.strip() for line in lines]
    return [line for line in stripped if line and not line.startswith('#')]


def _git_destname(repository):
    git_folder = repository.rsplit('/', 1)[1]
    if git_folder.endswith('.git'):
        return git_folder[:-4]
    else:
        return git_folder


class Repo(object):
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

    def _group_folder(self, folder):
        if self._prefix:
            return os.path.join(folder, self._prefix)
        else:
            return folder

    def clone(self, folder):
        group_folder = self._group_folder(folder)
        mkpath(group_folder)
        git_folder = _git_destname(self._repository)
        destination = os.path.join(group_folder, git_folder)
        if os.path.exists(destination):
            msg('IN %s SKIPPING %s' % (self._prefix, git_folder))
            return
        msg('IN %s CLONING %s' % (self._prefix, git_folder))
        git.clone_or_die(self._repository, destination)

    def fast_forward(self, folder):
        group_folder = self._group_folder(folder)
        git_folder = _git_destname(self._repository)
        destination = os.path.join(group_folder, git_folder)
        if not os.path.exists(destination):
            errordie('Can\'t fast forward missing repository: {}'.format(destination))
        msg('IN %s FAST FORWARDING %s' % (self._prefix, git_folder))
        git.fast_forward_or_die(destination)

    def as_line(self):
        if self._prefix:
            return '{} {}'.format(self._prefix, self._repository)
        else:
            return '. {}'.format(self._repository)

    def __eq__(self, other):
        if isinstance(other, Repo):
            return (
                self._repository == other._repository
                and
                self._prefix == other._prefix
            )
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.as_line()


class ReposFile(object):
    def __init__(self, stored_file):
        self._stored_file = stored_file
        self._repositories = [
            Repo.parse(line)
            for line in _trim(stored_file.readlines())]

    def clone(self, folder):
        for repo in self._repositories:
            repo.clone(folder)

    def fast_forward(self, folder):
        for repo in self._repositories:
            repo.fast_forward(folder)

    def add(self, repo):
        for existing in self._repositories:
            if repo == existing:
                errordie('Duplicate entry {}'.format(repo))
        self._repositories.append(repo)

    def save(self):
        lines = [repo.as_line()+'\n' for repo in self._repositories]
        self._stored_file.writelines(sorted(lines))


class RepoSet(object):
    def __init__(self, name, folder, stored_file):
        self._name = name
        self._reposfile = ReposFile(stored_file)
        self._folder = folder

    def clone(self):
        msg('CLONING SET {}'.format(self._name))
        self._reposfile.clone(self._folder)

    def fast_forward(self):
        msg('FAST FORWARD IN SET {}'.format(self._name))
        self._reposfile.fast_forward(self._folder)

    def add_and_clone(self, repository, prefix):
        msg('IN SET {}'.format(self._name))
        repo = Repo(repository=repository, prefix=prefix)
        self._reposfile.add(repo)
        self._reposfile.save()
        repo.clone(self._folder)
