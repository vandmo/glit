import os
from ConfigParser import ConfigParser
from repo import RepoSet
from utils import errordie


ERROR_1 = 'Can not figure out set name from filename {}'


class Config():
    def __init__(self):
        self._filename = os.path.expanduser('~/.plit/sets')
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
        return RepoSet(
            name=name,
            folder=os.path.expanduser(self._config.get(name, 'folder')),
            repositories_filename=os.path.expanduser(self._config.get(name, 'repositories'))
        )

    def get_all_sets(self):
        return [
            self._repo_set(set_name)
            for set_name in self._config.sections()
        ]

    def add_set(self, repositories_file, folder, name=None):
        if not name:
            if not repositories_file.endswith('.repositories'):
                errordie(ERROR_1.format(repositories_file))
            name = os.path.basename(repositories_file)[:-13]
        if self._config.has_section(name):
            errordie('Set "{}" already exists'.format(name))
        else:
            self._config.add_section(name)
        self._config.set(name, 'folder', folder)
        self._config.set(name, 'repositories', repositories_file)
        with open(self._filename, 'wb') as configfile:
            self._config.write(configfile)
