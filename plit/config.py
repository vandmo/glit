import os
from collections import OrderedDict
from yamlutils import load_yaml, save_as_yaml
from repo import RepoSet
from utils import errordie


ERROR_1 = 'Can not figure out set name from filename {}'


def _repo_set(config):
    return RepoSet(
        name=config['name'],
        folder=os.path.expanduser(config['folder']),
        repositories_filename=os.path.expanduser(config['repositories']))


class Config():
    def __init__(self):
        self._filename = os.path.expanduser('~/.plit/config.yaml')
        self._config = load_yaml(self._filename)

    def get_set_or_die(self, name):
        return self.get_set(name) or errordie('No such set "{}"'.format(name))

    def get_set(self, name):
        set_config = self._set_config_for(name)
        if set_config:
            return _repo_set(set_config)
        return None

    def _set_config_for(self, name):
        for set_config in self._config['sets']:
            if name == set_config['name']:
                return set_config
        return None

    def get_all_sets(self):
        return [_repo_set(set_config) for set_config in self._config['sets']]

    def add_set(self, repositories_file, folder, name=None):
        if not name:
            if not repositories_file.endswith('.repositories'):
                errordie(ERROR_1.format(repositories_file))
            name = os.path.basename(repositories_file)[:-13]
        if self._set_config_for(name):
            errordie('Set "{}" already exists'.format(name))
        entry = OrderedDict()
        entry['name'] = name
        entry['folder'] = folder
        entry['repositories'] = repositories_file
        self._config['sets'].append(entry)
        save_as_yaml(self._config, self._filename)
