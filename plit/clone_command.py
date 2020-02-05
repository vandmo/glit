from .config import Config
import click


@click.command(name='clone')
@click.argument('repository')
@click.option(
    '--to-set',
    required=True,
    help='The set to save the repository to')
@click.option('--prefix')
def command(repository, to_set, prefix):
    '''Clones a repository and adds it to a set'''
    config = Config()
    theset = config.get_set_or_die(to_set)
    theset.add_and_clone(repository=repository, prefix=prefix)
