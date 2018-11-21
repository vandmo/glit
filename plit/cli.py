import click

import all_command
import clone_command
import clone_all_command
import clone_set_command
import config_command


@click.group()
@click.version_option()
def cli():
    pass


cli.add_command(all_command.command)
cli.add_command(clone_command.command)
cli.add_command(clone_all_command.command)
cli.add_command(clone_set_command.command)
cli.add_command(config_command.command)
