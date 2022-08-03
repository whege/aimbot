__all__ = [
    "get_commands"
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
