import os
from ConfigParser import ConfigParser
from repo import RepoSet
from utils import errordie


ERROR_1 = 'Can not figure out set name from filename {}'


def _repo_set(name, items):
    return RepoSet(
        name=name,
        folder=os.path.expanduser(items['folder']),
        repositories_filename=os.path.expanduser(items['repositories']))


class Config():
    def __init__(self):
        self._filename = os.path.expanduser('~/.plit/sets')
        self._config = ConfigParser()
        if os.path.isfile(self._filename):
            self._config.read(self._filename)

    def get_set_or_die(self, name):
        return self.get_set(name) or errordie('No such set "{}"'.format(name))

    def get_set(self, name):
        set_config = self._set_config_for(name)
        if set_config:
            return _repo_set(name, set_config)
        return None

    def _set_config_for(self, name):
        if not self._config.has_section(name):
            return None
        return self._config.items(name)

    def get_all_sets(self):
        return [
            _repo_set(set_name, self._config.items(set_name))
            for set_name in self._config.sections()
        ]

    def add_set(self, repositories_file, folder, name=None):
        if not name:
            if not repositories_file.endswith('.repositories'):
                errordie(ERROR_1.format(repositories_file))
            name = os.path.basename(repositories_file)[:-13]
        if self._set_config_for(name):
            errordie('Set "{}" already exists'.format(name))
        if not self._config.has_section(name):
            self._config.add_section(name)
        self._config.set(name, 'folder', folder)
        self._config.set(name, 'repositories', repositories_file)
        with open(self._filename, 'wb') as configfile:
            self._config.write(configfile)
