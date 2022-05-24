from twitchbot import Command, Message


ADMIN_COMMAND_PERMISSION = 'admin'


@Command("ban")
async def cmd_fake_ban(msg: Message, *args):
    await msg.reply(
        f"{msg.author} is pretending to smack {args[0]} with the ban hammer for some dumb/sus/etc. "
        f"sh*t they did/said. It's just symbolic to pacify {msg.author}."
    )


@Command("bigmike", permission=ADMIN_COMMAND_PERMISSION)
async def cmd_so_mike(msg: Message):
    await msg.reply("YEPA YEPA!!!")


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


@Command("hug")
async def cmd_give_hug(msg: Message, *args):
    await msg.reply(f"{msg.author} gives {args[0]} a big ole bear hug! Thanks for being awesome!!!")


@Command("intel", permission=ADMIN_COMMAND_PERMISSION)
async def cmd_so_hens(msg: Message):
    await msg.reply("It's pronounced inteli-HENS twitch.tv/intelijens")


@Command("oof")
async def cmd_oof(msg: Message):
    await msg.reply("Oh noes, does wittle baby have a boo-boo? Come hewe and let mommy kiss it.")


@Command("raw", permission=ADMIN_COMMAND_PERMISSION)
async def cmd_so_raw(msg: Message):
    await msg.reply("That's Raw with a zero twitch.tv/raw0nline")


@Command("^")
async def cmd_this(msg: Message):
    await msg.reply("^^")


@Command("val", permission=ADMIN_COMMAND_PERMISSION)
async def cmd_so_val(msg: Message):
    await msg.reply("Hi loser twitch.tv/valkeryias")
