import telebot
from telebot import types
bot = telebot.TeleBot('6434991735:AAFfWYwjPPIzij07dM_ef8YTF4CtuSqYY_M')

@bot.message_handler(commands=['start', 'help'])
def start(message):

    keys = types.ReplyKeyboardMarkup(resize_keyboard=True)

    key_schedule = types.KeyboardButton("Расписание")
    key_statistics = types.KeyboardButton("Статистика")

    keys.add(key_schedule)
    keys.add(key_statistics)

    bot.send_message(message.from_user.id, 'Приветствую! Я могу показать тебе расписание на ближайшие матчи NBA, а так же показать стактистику игроков. \nНапиши /help, чтобы узнать больше!', reply_markup=keys)



#
def stats(player):
    keys = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton('Полная статистика')
    key2 = types.KeyboardButton('Очки')
    key4 = types.KeyboardButton('Подборы')
    key5 = types.KeyboardButton('Передачи')
    key6 = types.KeyboardButton('Перехваты')
    key7 = types.KeyboardButton('Блокшоты')
    return keys

@bot.message_handler(content_types=['text'])
def get_text_messaages(message):

    if message.text == 'Расписание' or message.text == 'Вернуться к выбору матчей':

        game = types.ReplyKeyboardMarkup(resize_keyboard=True)
        count = 5
        teams = ['team1', 'team2']

        for i in range(1,count+1):
            game.add(f'Матч №{i}: {teams[0]} vs {teams[1]}')

        game_back = types.KeyboardButton('Вернуться в меню')

        game.add(game_back)
        bot.send_message(message.from_user.id,'Выберите интересующий вас матч',reply_markup=game)

    elif message.text == 'Матч 1':
        bot.send_message(message.from_user.id,'team 1 - team2')
    elif message.text == 'Матч 2':
        bot.send_message(message.from_user.id,'team 1 - team2')
    elif message.text == 'Матч 3':
        bot.send_message(message.from_user.id,'team 1 - team2')
    elif message.text == 'Матч 4':
        bot.send_message(message.from_user.id,'team 1 - team2')

    elif message.text == 'Вернуться в меню':
        keys = types.ReplyKeyboardMarkup(resize_keyboard=True)

        key_schedule = types.KeyboardButton("Расписание")
        key_statistics = types.KeyboardButton("Статистика")

        keys.add(key_schedule)
        keys.add(key_statistics)
        bot.send_message(message.from_user.id, 'Что вы хотите посмотретть?',reply_markup=keys)


    elif message.text == 'Статистика' or message.text == 'Вернуться к игрокам':
        count = 5
        keys = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(1,count + 1):
            keys.add(f'Игрок {i}')
        key_back = types.KeyboardButton('Вернуться в меню')
        keys.add(key_back)
        bot.send_message(message.from_user.id, 'Выберите игрока', reply_markup=keys)



    elif message.text == 'Игрок 1':
        keys = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('Полная статистика')
        key2 = types.KeyboardButton('Очки')
        key3 = types.KeyboardButton('Подборы')
        key4 = types.KeyboardButton('Передачи')
        key5 = types.KeyboardButton('Перехваты')
        key6 = types.KeyboardButton('Блокшоты')
        key_back = types.KeyboardButton('Вернуться к игрокам')
        keys.add(key1, key2, key3, key4, key5, key6, key_back)
        bot.send_message(message.from_user.id, 'Выберите интересующую вас статистику',reply_markup=keys)



bot.polling(none_stop = True, interval = 0)

