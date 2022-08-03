__all__ = ["FUN_COMMANDS"]
__author__ = """whege"""
__date__ = "8/2/2022"
__doc__ = """Enter some text here, bitch"""

from twitchbot import Command, Message

from common.constants import VIP_PERMISSION
from common.utilfuncs import get_commands


@Command("ban")
async def cmd_fake_ban(msg: Message, *args):
    await msg.reply(
        f"{msg.author} is pretending to smack {args[0]} with the ban hammer for some dumb/sus/etc. "
        f"sh*t they did/said. It's just symbolic to pacify {msg.author}."
    )


@Command("cam")
async def cmd_cam_will(msg: Message):
    await msg.reply("CAM WILL CAM")


@Command("cancel")
async def cmd_cancel(msg: Message, *args):
    await msg.reply(
        f"{args[0]} is officially cancelled for doing or saying something sexist, misogynistic, or chauvinistic. "
        f"#cancel{args[0]}!"
    )


@Command("chair")
async def cmd_chair(msg: Message):
    await msg.reply("Oh me, Oh my!! My wifey needs me....... or I'm taking a massive poop 😎 It's the chair stream 😎")


@Command("comms")
async def cmd_comms(msg: Message):
    await msg.reply("comms comms comms comms comms comms comms comms comms comms comms comms comms comms comms comms "
                    "comms comms comms comms comms comms")


@Command("ele")
async def cmd_ele(msg: Message):
    await msg.reply("EVERYBODY LOVE EVERYBODY!")


@Command("gdo")
async def cmd_gdo(msg: Message):
    await msg.reply("GET DICK3D ON (this is Kay’s saying)")


@Command("hug")
async def cmd_give_hug(msg: Message, *args):
    await msg.reply(f"{msg.author} gives {args[0]} a big ole bear hug! Thanks for being awesome!!!")


@Command("kinky")
async def cmd_ima_kinda_kinky(msg: Message):
    await msg.reply(
        "Let this just sink in. Enjoy a laugh. https://clips.twitch.tv/DeterminedBoxyLemurBleedPurple-5RciHfzjh4f0jIQf "
    )


@Command("lb")
async def cmd_leaderboard(msg: Message):
    await msg.reply(
        "Don't even look at the leaderboard. Kendra won, just accept it. You suck, she's better."
    )


@Command("lng")
async def cmd_lng(msg: Message):
    await msg.reply(
        "We are the LATE NITE GANG! We stay up too late and our sleep schedules are fucked but we always have a good "
        "time. "
    )


@Command("onlyfans")
async def cmd_only_fans(msg: Message):
    await msg.reply(
        "Make sure to sub for VIP access to my exclusive onlyfans BrokeBack"
    )


@Command("oof")
async def cmd_oof(msg: Message):
    await msg.reply("Oh noes, does wittle baby have a boo-boo? Come hewe and let mommy kiss it.")


@Command("poo")
async def cmd_poo(msg: Message, *args):
    await msg.reply(
        f"{msg.author} poops in their hand and throws it at {args[0]} like an angry monkey! 🐵 💩"
    )


@Command("sas", permission=VIP_PERMISSION)
async def cmd_sas(msg: Message):
    await msg.reply("Puro Pinche SAS!")


@Command("sheesh")
async def cmd_sheesh(msg: Message):
    await msg.reply("SHEEEEEEEEEEEEESH")


@Command("slap")
async def cmd_slap(msg: Message, *args):
    await msg.reply(
        f"{msg.author} raises their hand slowly, then like Mr Miyagi, they strike {args[0]} so quick and fierce that "
        f"they are not even certain from what direction they were slapped. "
    )


@Command("sleep")
async def cmd_sleep(msg: Message):
    await msg.reply("I am an old man so I’m going to sleep. I’ll dream about your juicy donk GivePLZ TakeNRG")


@Command("tickle")
async def cmd_tickle(msg: Message, *args):
    await msg.reply(
        f"{msg.author} sneaks up and tickles {args[0]}. It’s funny at first, but spirals out of control until "
        f"{args[0]} pisses themselves. Now it’s awkward. Nice! "
    )


FUN_COMMANDS = get_commands()
