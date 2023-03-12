import pandas as pd
import telegram

# read excel file
df = pd.read_excel('file.xlsx')

# select first 100 phone numbers
numbers = df['phone_number'][:100]

# create bot object
bot = telegram.Bot(token='3e6b348fe5c842b112967592c60201d9')
chat_id = YOUR_GROUP_CHAT_ID

# add phone numbers to group
for number in numbers:
    bot.add_chat_member(chat_id=chat_id, user_id=number)
