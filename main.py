from parsing_and_api import *
from game import *
from bot import *
button_list = ["Случайная цитата", "Неофициальное API IMDB", 'Игра']
@bot.message_handler(commands=['start'])
def start_menu(message):
    bot.send_message(message.from_user.id, "Привет! Я тестовый бот для курса программирования на языке ПаЙтон", reply_markup=keyboard(button_list))
    users.update({message.from_user.id:{}})

@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    if call.data == "Случайная цитата":
        bot.send_message(call.from_user.id,parsing())
    if call.data == "Неофициальное API IMDB":
        random_item = get_api()['items'][random.randint(0,250)]
        bot.send_photo(call.from_user.id, random_item['image'],f'{random_item["fullTitle"]}\nРейтинг-{random_item["imDbRating"]}')
    if call.data == "Игра":
        bot.send_message(call.from_user.id, "Идет поиск игры!")
        search_game(call)

@bot.message_handler(content_types=["text"], func = lambda message:users[message.from_user.id]['teammate'] is not None)
def game(message):
    bot.send_message(users[message.from_user.id]['teammate'],message.text)
    if users[message.from_user.id]['word'].lower() in message.text.lower():
        bot.send_message(users[message.from_user.id]['teammate'], f"Победил {message.from_user.username}!",reply_markup=keyboard(button_list))
        bot.send_message(message.from_user.id, f"Вы победили!", reply_markup=keyboard(button_list))



bot.infinity_polling()
