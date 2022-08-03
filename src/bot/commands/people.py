__all__ = ["PPL_COMMANDS"]
__author__ = """whege"""
__date__ = "8/2/2022"
__doc__ = """Fun commands for games"""

from twitchbot import Command, Message

from common.constants import ADMIN_PERMISSION
from common.utilfuncs import get_commands


@Command("bigmike", permission=ADMIN_PERMISSION)
async def cmd_so_mike(msg: Message):
    await msg.reply("YEPA YEPA!!!")


@Command("blake", permission=ADMIN_PERMISSION)
async def cmd_so_blake(msg: Message):
    await msg.reply("Fucking cutie, he’s cracked at warzone my guy! Hoooyyyeeeaaaahhhhh!")


@Command("bully")
async def cmd_sage_the_bully(msg: Message):
    await msg.reply("Oh ................hey..... it's .... SageTHEBULLY..........")


@Command("engin")
async def cmd_engin(msg: Message):
    await msg.reply("EnginEarz hates being bullied by Mezdie a lot, but Mezdie likes bullying him, more than that!")


@Command("intel", permission=ADMIN_PERMISSION)
async def cmd_so_hens(msg: Message):
    await msg.reply("It's pronounced inteli-HENS twitch.tv/intelijens")


@Command("kay")
async def cmd_so_kay(msg: Message):
    await msg.reply(
        "THE ONE AND ONLY FOUNDER. THE LEGEND IN THE FLESH THE GOD TIER OWNER OF THE PHRASE 'GET DICKED ON' IS HERE!"
    )


@Command("kendra")
async def cmd_so_kendra(msg: Message):
    await msg.reply(
        "Queen Supreme of the Moderators and wife of Mezdie the Breaker of Spirits. She’s way nicer than him, "
        "but we still don’t recommend getting on her bad side! "
    )


@Command("mezdie")
async def cmd_so_mezdie(msg: Message):
    await msg.reply("Many fear him. Few understand him. Even fewer love him. Which one are you?")


@Command("raw", permission=ADMIN_PERMISSION)
async def cmd_so_raw(msg: Message):
    await msg.reply("That's Raw with a zero twitch.tv/raw0nline")


@Command("ryan")
async def cmd_so_ryan(msg: Message):
    await msg.reply("Real man eat rice with chopstick like Ryan-san")


@Command("sage")
async def cmd_so_ryan(msg: Message):
    await msg.reply("Just some random bot")


@Command("sponsor")
async def cmd_sponsor(msg: Message):
    await msg.reply("Be a dear and get mommy something sweet: https://www.instagram.com/andreas_sweetbakes/")


@Command("val", permission=ADMIN_PERMISSION)
async def cmd_so_val(msg: Message):
    await msg.reply("Hi loser twitch.tv/valkeryias")


@Command("zimbo", permission=ADMIN_PERMISSION)
async def cmd_so_zimbo(msg: Message):
    await msg.reply("If you need hilarious comms, 647 damage with 2 kills, and a damn barrel of laughs, call Zimbo. "
                    "He’s always ready to drop in and break his legs!"
                    )


PPL_COMMANDS = get_commands()
