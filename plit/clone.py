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
    pass
