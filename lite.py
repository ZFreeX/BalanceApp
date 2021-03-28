from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsSearch

api_id = 3197610
api_hash = '62ce61002c315fc235c862418e40c0f0'

# url = 'https://BalanceApp.pythonanywhere.com/secret_url'
client = TelegramClient('zbot', api_id, api_hash).start(
    bot_token="1663187056:AAGAgxjWy2W3fOArw_wg6m0AYpl03Zhx54I")


phone_number = '+375256938241'
################################################
channel_username = 'second228'
################################################





assert client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))



# ---------------------------------------
offset = 0
limit = 200
my_filter = ChannelParticipantsSearch('')
all_participants = []
while_condition = True
# ---------------------------------------
channel = client(GetFullChannelRequest(channel_username))
while while_condition:
    participants = client(GetParticipantsRequest(channel=channel_username, filter=my_filter, offset=offset, limit=limit, hash=0))
    all_participants.extend(participants.users)
    offset += len(participants.users)
    if len(participants.users) < limit:
         while_condition = False



print(all_participants)