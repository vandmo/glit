import click
from .config import config


@click.command(name='clone-all')
def command():
    '''Clones all sets'''
    sets = config.get_all_sets()
    for aset in sets:
        aset.clone()
