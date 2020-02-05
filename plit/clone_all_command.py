import click
from .config import Config


@click.command(name='clone-all')
def command():
    '''Clones all sets'''
    config = Config()
    sets = config.get_all_sets()
    for aset in sets:
        aset.clone()
