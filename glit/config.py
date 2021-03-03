import os
from configparser import ConfigParser
from .repo import RepoSet
from . import gitstorage
from . import localstorage
from .utils import errordie


ERROR_1 = 'Can not figure out set name from filename {}'
ERROR_2 = 'Invalid storage {}'
ERROR_3 = 'Set "{}" already exists'
ERROR_4 = 'No such file "{}" in "{}"'


class Config():
    def __init__(self):
        self._filename = os.path.expanduser('~/.glit/sets')
        self._config = ConfigParser()
        if os.path.isfile(self._filename):
            self._config.read(self._filename)

    def get_set_or_die(self, name):
        return self.get_set(name) or errordie('No such set "{}"'.format(name))

    def get_set(self, name):
        if not self._config.has_section(name):
            return None
        else:
            return self._repo_set(name)

    def _repo_set(self, name):
        storage = self._config.get(name, 'storage')
        if storage == 'git':
            return RepoSet(
                name=name,
                folder=os.path.expanduser(self._config.get(name, 'folder')),
                stored_file=gitstorage.GitStoredFile(
                    repository=self._config.get(name, 'repository'),
                    filename=self._config.get(name, 'file')
                )
            )
        elif storage == 'local':
            return RepoSet(
                name=name,
                folder=os.path.expanduser(self._config.get(name, 'folder')),
                stored_file=localstorage.LocallyStoredFile(
                    filename=os.path.expanduser(self._config.get(name, 'file'))
                )
            )
        else:
            errordie(ERROR_2.format(storage))

    def get_set_names(self):
        return self._config.sections()

    def get_all_sets(self):
        return [
            self._repo_set(set_name)
            for set_name in self.get_set_names()
        ]

    def _get_existing_set(self, name, filename):
        if not name:
            if not filename.endswith('.repositories'):
                errordie(ERROR_1.format(filename))
            name = os.path.basename(filename)[:-13]
        if self._config.has_section(name):
            errordie(ERROR_3.format(name))
        else:
            self._config.add_section(name)
        return name

    def add_git_stored_set(self, folder, name, repository, filename):
        name = self._get_existing_set(name, filename)
        stored_file = gitstorage.GitStoredFile(
            repository=repository, filename=filename)
        if not stored_file.exists():
            errordie(ERROR_4.format(filename, repository))
        self._config.set(name, 'folder', folder)
        self._config.set(name, 'storage', 'git')
        self._config.set(name, 'repository', repository)
        self._config.set(name, 'file', filename)
        self._save()

    def add_locally_stored_set(self, folder, name, filename):
        name = self._get_existing_set(name, filename)
        self._config.set(name, 'folder', folder)
        self._config.set(name, 'storage', 'local')
        self._config.set(name, 'file', filename)
        self._save()

    def _save(self):
        with open(self._filename, 'wb') as configfile:
            self._config.write(configfile)


config = Config()
