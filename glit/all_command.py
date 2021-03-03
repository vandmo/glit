import click
from .config import config


@click.group(name='all')
def command():
    '''Do things for all repositories'''
    pass


@command.command(name='fast-forward')
def fast_forward():
    '''Does git pull --ff-only for all repositories'''
    sets = config.get_all_sets()
    for aset in sets:
        aset.fast_forward()
