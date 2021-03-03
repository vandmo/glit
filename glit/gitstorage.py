from . import git
import os
from urllib.parse import quote_plus
from .utils import msg


_CACHE_FOLDER = os.path.expanduser('~/.glit/cache/git/')


_already_pulled = set()


class GitStoredFile(object):
    def __init__(self, repository, filename):
        self._repository = repository
        self._relative_filename = filename
        cache_name = quote_plus(repository)
        self._local_location = os.path.join(_CACHE_FOLDER, cache_name)
        self._full_filename = os.path.join(self._local_location, filename)

    def _pull(self):
        if self._repository in _already_pulled:
            return
        if os.path.isdir(self._local_location):
            msg('Updating {}'.format(self._repository))
            git.fast_forward_or_die(self._local_location)
        else:
            msg('Cloning {}'.format(self._repository))
            git.clone_or_die(self._repository, self._local_location)
        _already_pulled.add(self._repository)

    def _push(self):
        git.commit_or_die(
            repository=self._local_location,
            filename=self._relative_filename,
            message='Updated by glit')
        git.push_or_die(self._local_location)

    def exists(self):
        self._pull()
        return os.path.isfile(self._full_filename)

    def readlines(self):
        self._pull()
        with open(self._full_filename) as f:
            return f.readlines()

    def writelines(self, lines):
        self._pull()
        with open(self._full_filename, 'w') as f:
            f.writelines(lines)
        self._push()
