import subprocess
from .utils import errordie


def _call_or_die(args, cwd=None):
    status = subprocess.call(['git']+args, cwd=cwd)
    if status:
        errordie('git failed with {}'.format(status))


def clone_or_die(repository, destination=None):
    args = ['clone', repository]
    if destination is not None:
        args.append(destination)
    _call_or_die(args)


def fast_forward_or_die(repository):
    _call_or_die(['pull', '--ff-only'], repository)


def push_or_die(repository):
    _call_or_die(['push'], repository)


def add_all_or_die(repository):
    _call_or_die(['add', '.'], repository)


def commit_or_die(repository, filename, message):
    args = list()
    args.append('commit')
    args.append('--message='+message)
    args.append(filename)
    _call_or_die(args, repository)
