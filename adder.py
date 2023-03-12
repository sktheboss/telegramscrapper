#!/bin/env python3
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import random

api_id =   '29888795' #Enter Your 7 Digit Telegram API ID.
api_hash = '6059a426270201ccaab88dd5160cdde5'   #Enter Yor 32 Character API Hash
phone = '+919162716778'   #Enter Your Mobilr Number With Country Code.
client = TelegramClient(phone, api_id, api_hash)
async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello !!!!!')


SLEEP_TIME_1 = 100
SLEEP_TIME_2 = 9792
with client:
    client.loop.run_until_complete(main())
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('40779'))

users = list()
with open(r"C:\\Users\\Suraj\\Desktop\\telegramscraper\\members\\mem_user.csv", encoding='UTF-8') as f:  #Enter your file name
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {
            'username': row[0],
            # 'id': int(row[1]),
            # 'access_hash': int(row[2]),
            # 'name': row[3],
        }

        users.append(row[0])

chats = []
last_date = None
chunk_size = 900
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print('Choose a group to add members: ')
for i, group in enumerate(groups):
    print(str(i) + '- ' + group.title)
g_index = "aapkifree" #input("Enter a Number: ")
target_group = client.get_entity(g_index)#groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

#mode = int(input("Enter 1 to add by username or 2 to add by ID: "))
mode=2
n = 0
# while users:
#     chunk, users = users[:30], users[30:]
#     print("Going for below users")
#     print(chunk)
#     time.sleep(400)
#     try:
#         client(InviteToChannelRequest(target_group_entity, users=chunk))
#     except PeerFloodError:
#             print("[error] Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
#             print("[info] Waiting {} seconds".format(SLEEP_TIME_2))
#             time.sleep(SLEEP_TIME_2)
#     except UserPrivacyRestrictedError:
#         print(f"[error] The [userid]=[{user['id']}] user's privacy settings do not allow you to do this. Skipping ...")
#         print("[info] Waiting for 5 Seconds ...")
#         time.sleep(random.randrange(0, 5))
#     except:
#         traceback.print_exc()
#         print("[error] Unexpected Error! ")

for user in users:
    n += 1
    if n % 80 == 0:
        time.sleep(60)
    try:
        print("Adding {}".format(user))
        # if user['username'] != "":
        user_to_add = client.get_input_entity(user)
        # else:
            # user_to_add = InputPeerUser(user['id'], user['access_hash'])

        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("Waiting for 60-180 Seconds ...")
        time.sleep(random.randrange(10, 20))
    except PeerFloodError:
        print("[error] Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        print("[info] Waiting {} seconds".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except UserPrivacyRestrictedError:
        print(f"[error] The [userid]=[{user}] user's privacy settings do not allow you to do this. Skipping ...")
        print("[info] Waiting for 5 Seconds ...")
        time.sleep(random.randrange(0, 5))
    except:
        traceback.print_exc()
        print("[error] Unexpected Error! ")
        continue