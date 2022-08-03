__all__ = ["GAME_COMMANDS"]
__author__ = """whege"""
__date__ = "8/2/2022"
__doc__ = """Fun commands for games"""

from random import choice, randrange

from twitchbot import Command, Message

from common.utilfuncs import get_commands


@Command("flip")
async def cmd_flip_coin(msg: Message):
    await msg.reply(f"{msg.author} flips a coin, and it's....{'heads' if choice([0, 1]) == 1 else 'tails'}!")


@Command("roll")
async def cmd_roll_die(msg: Message, n: str):
    n = int(n)

    if n <= 1:
        await msg.reply(f'Hey {msg.author}, how do you expect to roll a {n}-sided die, moron? FBPenalty')
    else:
        await msg.reply(f"{msg.author} rolled a {n}-sided die and got....{randrange(1, n+1)}")


@Command("rpc")
async def cmd_rock_paper_scissors(msg: Message, play: str = None):
    moves = ["rock", "paper", "scissors"]

    if play is None:
        await msg.reply(
            f"Hey {msg.author}, include your move, dumbass."
        )
        return

    elif play not in moves:
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


GAME_COMMANDS = get_commands()
