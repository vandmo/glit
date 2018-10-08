from collections import OrderedDict

import yaml


def save_as_yaml(value, target_filename):
    with open(target_filename, 'w') as target_file:
        ordered_dump(
            value,
            target_file,
            Dumper=yaml.SafeDumper,
            default_flow_style=False,
            allow_unicode=True,
            encoding='utf-8')


def load_yaml(filename):
    with open(filename, 'rb') as f:
        return ordered_load(f, yaml.SafeLoader)


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)


def ordered_dump(data, stream=None, Dumper=yaml.Dumper, **kwds):
    class OrderedDumper(Dumper):
        pass

    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())
    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)
