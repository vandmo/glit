import click

import clone
import clone_all
import clone_set


@click.group()
@click.version_option()
def cli():
    pass


cli.add_command(clone.command)
cli.add_command(clone_all.command)
cli.add_command(clone_set.command)
