from .config import config
import click


@click.command(name='clone-set')
@click.option('--name', required=True, prompt=True, type=click.Choice(config.get_set_names()))
def command(name):
    '''Clones a specific sets'''
    set_ = config.get_set_or_die(name)
    set_.clone()
