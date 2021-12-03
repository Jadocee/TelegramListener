from telethon import TelegramClient, events, sync

api_id = 17750229
api_hash = '89fcee77ecb687982d7b6ead0377b5ea'
bot_token = '5056263480:AAFC0OBoY9w1s8gz58G5bv0s_sWIn70shC4'

CMC = 'https://t.me/CMC_fastest_alerts'

client = TelegramClient('user', api_id, api_hash)





async def main():
    await client.start(phone='+61447905599', password='4ciiNFWBivjdZWaj5TtP')


    me = await client.get_me()

    print(me.stringify() + "\n")

    username = me.username
    print(username)
    print(me.phone)
    print('🔴')

    @client.on(events.NewMessage(CMC))
    async def event_listener(event):
        await client.forward_messages('https://t.me/adafadfa', event.message)
        content = event.message.raw_text
        print(content)
        views = event.views


        print(event.stringify() + '\n')
        print(event.message.text)



#async def listen():
   # await client.on(event=events.NewMessage(incoming=True, chats=CHANNEL))




# @client.on(events.NewMessage(chats="@dasfqasdfd"))
# async def event_listener(event):
# print(event.message.message)

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
