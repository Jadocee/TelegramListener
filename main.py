from telethon import TelegramClient, events, sync
import json
import os
from pathlib import Path

if os.path.isfile(path=Path('config.json')) is False:
    api_id = int(input('Enter your App api_id: '))
    api_hash = input('Enter your App api_hash: ')

    app = {
        "api_id": api_id,
        "api_hash": api_hash
    }

    json_obj = json.dumps(app, indent=4, sort_keys=True)
    with open("config.json", 'w') as out:
        out.write(json_obj)

if os.path.isfile(path=Path('account.json')) is False:
    phone = input("Enter your phone number: ")
    tfa = ''
    while tfa.lower() != 'y' and tfa.lower() != 'n':
        tfa = input("Is 2FA enabled for this number? (Y/n): ")
    if tfa.lower() == 'y':
        password = input("Enter your password: ")
    else:
        password = ''

    account = {
        "phone": phone,
        "password": password
    }

    json_obj = json.dumps(account, indent=4, sort_keys=True)
    with open('account.json', 'w') as out:
        out.write(json_obj)

with open('config.json', 'r') as f:
    config_obj = json.load(fp=f)

with open('account.json', 'r') as f:
        acc = json.load(f)

client = TelegramClient('user', config_obj['api_id'], config_obj['api_hash'])\
    .start(phone=acc['phone'], password=acc['password'])


async def main():
    user = await client.get_me()
    choice = 0
    print('-------------------------------------------------------------')
    print("Select a channel to listen to: ")
    print('1.\tCoinmarketcap Fastest Alerts')
    print('2.\tCoingecko Fastest Alerts')
    print('3.\tCustom')
    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input('Choice: '))
    if choice == 1:
        channel_link = 'https://t.me/CMC_fastest_alerts'
    elif choice == 2:
        channel_link = 'https://t.me/CG_fastest_alerts'
    else:
        channel_link = input('Enter the channel link: ')

    @client.on(events.NewMessage(channel_link))
    async def event_listener(event):
        print(event.message.text)
        if event.views is not None:
            print('This message has been viewed ' + event.views + ' times.')

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
