from telethon import TelegramClient, events, sync


class Listener:

    def __init__(self, new_client: TelegramClient, new_channel: str, new_link: str):
        self.client = new_client
        self.channel = new_channel
        self.link = new_link

