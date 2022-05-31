import random
import time
users={}
from bot import *
def search_game(call):
    users.update({call.from_user.id:{'word':get_word(),'username': call.from_user.username,'teammate':None}})
    for i in users.keys():
        print(users)
        if users[i]['teammate'] is None and i !=call.from_user.id:
            users[i]['teammate'] = call.from_user.id
            users[call.from_user.id]['teammate'] = i
            bot.send_message(call.message.chat.id,f"Вы играете с {users[users[call.from_user.id]['teammate']]['username']}\nЕго слово* {users[users[call.from_user.id]['teammate']]['word']}*",parse_mode='Markdown')
            bot.send_message(users[call.from_user.id]['teammate'],f"Вы играете с {call.from_user.username}\nЕго слово* {users[call.from_user.id]['word']}*",parse_mode='Markdown')

def get_word():
    with open("words.txt","r",encoding='utf-8') as text:
        return random.choice(text.readline().split())

