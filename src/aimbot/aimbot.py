from twitchbot import BaseBot, Channel


class MommyTron(BaseBot):
    async def on_channel_joined(self, channel: Channel):
        await channel.send_message("Don't worry, mommy is here! MercyWing1 PinkMercy MercyWing2")


MommyTron().run()
