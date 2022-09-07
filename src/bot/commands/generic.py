__all__ = ["GEN_COMMANDS"]
__author__ = """whege"""
__date__ = "8/2/2022"
__doc__ = """Enter some text here, bitch"""

from twitchbot import Command, Message

from common.constants import MODERATOR_PERMISSION
from common.utilfuncs import get_commands, shoutout


def raid_message(emote: str) -> str:
    """
    Create a raid message with the provided emote
    :param emote: emote to be used in the message
    :return: Formatted raid message
    """
    return " ".join(["IT'S A RAID-AR", emote, emote, emote] * 5)


@Command("discord")
async def cmd_discord(msg: Message):
    await msg.reply("https://discord.gg/juwzKrw5Ar")


@Command("doggos")
async def cmd_doggos(msg: Message):
    await msg.reply("Teddy: Black Lab Mix; George: Goldendoodle")


@Command("fr", permission=MODERATOR_PERMISSION)
async def cmd_follower_raid(msg: Message):
    await msg.reply(raid_message("r4d4rlCatDance"))


@Command("lg")
async def cmd_lfg(msg: Message):
    await msg.reply("LETS GOOOOOO!!")


@Command("lurk")
async def cmd_lurk(msg: Message):
    await msg.reply(
        f"Lurking is not only appreciated but encouraged! Thanks for the support, {msg.author}!"
    )


@Command("peripherals")
async def cmd_peripherals(msg: Message):
    await msg.reply(
        "Acer Nitro XF3 | HyperX Alloy Origins Core TKL | HyperX Pulsefire Haste | HyperX Cloud II Wireless "
        "| Noblechairs EPIC Series "
    )


@Command("poll", permission=MODERATOR_PERMISSION)
async def cmd_poll(msg: Message):
    await msg.reply("HEY YOU. THERE'S A POLL. GO VOTE YOU BOT")


@Command("so", permission=MODERATOR_PERMISSION)
async def cmd_shoutout(msg: Message, *args):
    await msg.reply(shoutout(args[0]))


@Command("specs")
async def cmd_specs(msg: Message):
    await msg.reply(
        "MSI BPG B550 Gaming Plus | AMD Ryzen 7 3700X | MSI ARMOR OC Radeon RX 580 | 500 TB WD Blue M.2 SSD | 1 TB WD "
        "Blue HDD16 GB Team Dark RAM "
    )


@Command("sr", permission=MODERATOR_PERMISSION)
async def cmd_sub_raid(msg: Message):
    await msg.reply(raid_message("r4d4rlRaid"))


@Command("talk")
async def cmd_cant_talk(msg: Message):
    await msg.reply("A viewer redeemed an IRL voice ban...I can't talk until the match is over Sadge")


@Command("^", prefix="")
async def cmd_this(msg: Message):
    await msg.reply("^^")


GEN_COMMANDS = get_commands()
