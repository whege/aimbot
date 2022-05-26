from random import choice, randrange

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


@Command("flip")
async def cmd_flip_coin(msg: Message):
    await msg.reply(f"{msg.author} flips a coin, and it's....{'heads' if choice([0, 1]) == 1 else 'tails'}!")


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


@Command("roll")
async def cmd_roll_die(msg: Message, n: str):
    n = int(n)

    if n <= 1:
        await msg.reply(f'Hey {msg.author}, how do you expect to roll a {n}-sided die, moron? FBPenalty')
    else:
        await msg.reply(f"{msg.author} rolled a {n}-sided die and got....{randrange(1, n+1)}")


@Command("rpc")
async def cmd_rock_paper_scissors(msg: Message, play: str):
    moves = ["rock", "paper", "scissors"]

    if play not in moves:
        await msg.reply(
            f"Hey {msg.author}, that's not a valid move, idiot. The game is called 'Rock, Paper, Scissors'."
        )
        return
    else:
        bot_move = choice(moves)

    if bot_move == "rock":
        if play == "rock":
            result = "tie"
        elif play == "paper":
            result = "win"
        else:
            result = "lose"

    elif bot_move == "paper":
        if play == "rock":
            result = "lose"
        elif play == "paper":
            result = "tie"
        else:
            result = "win"

    else:
        assert bot_move == "scissors"
        if play == "rock":
            result = "lose"
        elif play == "paper":
            result = "win"
        else:
            result = "tie"

    if result == "tie":
        txt = " too...can't win em all I guess..."

    elif result == "win":
        txt = ". You win.... NotLikeThis But that was just luck..."

    else:
        txt = "! Sorry loser LUL"

    await msg.reply(f"I picked {bot_move}{txt}")


@Command("^")
async def cmd_this(msg: Message):
    await msg.reply("^^")


@Command("val", permission=ADMIN_COMMAND_PERMISSION)
async def cmd_so_val(msg: Message):
    await msg.reply("Hi loser twitch.tv/valkeryias")
