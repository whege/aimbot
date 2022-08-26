__all__ = []
__author__ = """whege"""
__date__ = "8/2/2022"
__doc__ = """Enter some text here, bitch"""

from twitchbot import BaseBot, Channel, Message


class MommyTron(BaseBot):
    async def on_bits_donated(self, msg: Message, bits: int):
        await msg.reply(
            f"{msg.author} cheered {bits} bits! What a sweetie!"
        )

    async def on_channel_joined(self, channel: Channel) -> None:
        """
        Message sent when the bot joins a channel
        :param channel: Channel to be joined
        :return: None
        """
        await channel.send_message("Don't worry, mommy is here! MercyWing1 PinkMercy MercyWing2")

    async def on_channel_raided(self, channel: Channel, raider: str, viewer_count: int) -> None:
        """
        Actions taken when the channel is raided
        :param channel: Currently joined channel
        :param raider: Channel that raided
        :param viewer_count: Number of viewers in the raid
        :return: None
        """
        await channel.send_message(f"OMFG {raider} JUST RAIDED WITH {viewer_count} viewers!!! LFG")
        await channel.send_message(f"!so @{raider}")

    def __call__(self, *args, **kwargs):
        self.run()


if __name__ == '__main__':
    # TODO add handling for when token is expired
    MommyTron()()
