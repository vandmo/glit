from config import Config
import click


@click.command(name='clone-set')
@click.argument('name')
def command(name):
    '''Clones a specific sets'''
    config = Config()
    set_ = config.get_set(name)
    set_.clone()
