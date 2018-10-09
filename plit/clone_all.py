from config import Config
import click


@click.command(name='clone-all')
def command():
    '''Clones all sets'''
    config = Config()
    sets = config.get_all_sets()
    for aset in sets:
        aset.clone()
