import click
from config import Config


@click.group(name='config')
def command():
    '''Group of commands related to configuration'''
    pass


@command.command(name='add-set')
@click.argument('repositories')
@click.option('--folder', required=True)
@click.option('--name')
def add_set(repositories, folder, name):
    '''Adds a repository set to the configuration file'''
    config = Config()
    config.add_set(repositories, folder, name)
