from telethon import TelegramClient, events, sync


class Listener:

    def __init__(self, new_client: TelegramClient, new_link: str):
        self.channel = None
        self.client = new_client
        self.channel_link = new_link

    async def start(self):
        self.channel = await self.client.get_entity(self.channel_link)

        @self.client.on(events.NewMessage(self.channel_link))
        async def event_listener(event):
            print(event.message.text)
            if event.views is not None:
                print('This message has been viewed ' + event.views + ' times.')


