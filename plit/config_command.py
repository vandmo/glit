import click
from config import Config


@click.group(name='config')
def command():
    '''Group of commands related to configuration'''
    pass


@command.command(name='add-locally-stored-set')
@click.argument('file')
@click.option('--folder', required=True)
@click.option('--name')
def add_set(file, folder, name):
    '''Adds a locally stored repository set to the configuration file'''
    config = Config()
    config.add_locally_stored_set(folder=folder, name=name, filename=file)


@command.command(name='add-git-stored-set')
@click.argument('repository')
@click.argument('file')
@click.option('--folder', required=True)
@click.option('--name')
def add_git_stored_set(repository, file, folder, name):
    '''Adds a git stored repository set to the configuration file'''
    config = Config()
    config.add_git_stored_set(
        folder=folder,
        name=name,
        repository=repository,
        filename=file)
