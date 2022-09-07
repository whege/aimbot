__all__ = [
    "get_commands",
    "shoutout"
]
__author__ = """whege"""
__date__ = "8/2/2022"
__doc__ = """Enter some text here, bitch"""

from inspect import getmembers, stack
from sys import modules
from typing import List

from twitchbot import Command


def get_commands() -> List[Command]:
    """
    Returns a list of the Command objects in the calling module

    :return:
    """
    caller = modules[stack()[1].frame.f_locals['__name__']]
    command_funcs = [f for _, f in getmembers(caller) if isinstance(f, Command)]
    assert len(command_funcs) > 0
    return command_funcs


def shoutout(account: str) -> str:
    """
    Creates a shoutout message for the passed user
    :param account:
    :return:
    """
    return f"Be a good boy and go follow {account} for mommy. " \
           f"They're such a nice kid. https://twitch.tv/{str(account).replace('@', '')}"
