__all__ = ["QUOTES"]
__author__ = """whege"""
__date__ = "8/2/2022"
__doc__ = """Enter some text here, bitch"""

from requests import get, post

from twitchbot import Command, Message

from common.utilfuncs import get_commands


@Command("bender")
async def cmd_bender(msg: Message):
    """
    Fetch random Futurama quote
    :param msg:
    :return:
    """
    quote = get("https://bender.sierrasoftworks.com/api/v1/quote").json()

    await msg.reply(f"'{quote['quote']}' -{quote['who']}")


QUOTES = get_commands()
