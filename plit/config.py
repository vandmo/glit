import os
from yamlutils import load_yaml
from repo import RepoSet


def _repo_set(config):
    return RepoSet(
        name=config['name'],
        folder=os.path.expanduser(config['folder']),
        repositories_filename=os.path.expanduser(config['repositories']))


class Config():
    def __init__(self):
        filename = os.path.expanduser('~/.plit/config.yaml')
        self._config = load_yaml(filename)

    def get_set(self, name):
        for set_config in self._config['sets']:
            if name == set_config['name']:
                return _repo_set(set_config)
        return None

    def get_all_sets(self):
        return [_repo_set(set_config) for set_config in self._config['sets']]
