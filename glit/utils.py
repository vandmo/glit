import click
import os
import sys


def mkpath(path):
    if not os.path.exists(path):
        os.makedirs(path)


def msg(message):
    click.echo(click.style('glit:', fg='cyan') + ' ' + message)


def warn(message):
    click.echo(click.style('glit[WARNING]:', fg='yellow') + ' ' + message)


def errordie(message, code=-1):
    click.echo(click.style('glit:', fg='red') + ' ' + message, err=True)
    sys.exit(code)
