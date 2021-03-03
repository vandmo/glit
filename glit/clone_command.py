from .config import config
import click


@click.command(name='clone')
@click.argument('repository')
@click.option(
    '--to-set',
    required=True,
    prompt=True,
    type=click.Choice(config.get_set_names()),
    help='The set to save the repository to')
@click.option('--prefix', default='', prompt=True)
def command(repository, to_set, prefix):
    '''Clones a repository and adds it to a set'''
    theset = config.get_set_or_die(to_set)
    theset.add_and_clone(repository=repository, prefix=prefix)
