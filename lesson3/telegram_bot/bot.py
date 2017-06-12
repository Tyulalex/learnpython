import logging
import ephem
import re
from setup import API_KEY
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    updater = Updater(API_KEY)
    dp = updater.dispatcher
    #dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_handler(CommandHandler("goroda", play_in_cities, pass_args=True))
    dp.add_handler(CommandHandler("planet", tell_constellation, pass_args=True))
    dp.add_handler(CommandHandler("wordcount", wordcount, pass_args=True))
    dp.add_handler(CommandHandler("calc", welcome_to_calculator))
    dp.add_handler(MessageHandler([Filters.text], calculator))
    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()


def welcome_to_calculator(bot, update):
    bot.sendMessage(update.message.chat_id, text='Добро пожаловать в калькулятор! Введите операцию в формате 3/5=. '
                                                 'Для выхода из режима калькулятора, нажмите /exitcalc')


def calculator(bot, update):

    operators_map={
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
        '*': lambda x, y: x*y,
        '/': lambda x, y: x/y
        }

    word_operators_map = {
        'плюс': '+',
        'минус': '-',
        'умножить на': '*',
        'поделить на': '/'
    }

    word_digit_map = {
        'ноль': 0,
        'один': 1,
        'два': 2,
        'три': 3,
        'четыре': 4,
        'пять': 5,
        'шесть': 6,
        'семь': 7,
        'восемь': 8,
        'девять': 9,
        'десять': 10
    }


    user_text = update.message.text


    is_match_digits = re.match('^(\d+)(\/|-|\+|\*)(\d+)=$', user_text)

    is_match_word = re.match(('^[С][с]колько будет (\w+) (плюс|минус|поделить на|умножить на) (\w+)$'), user_text)

    if not is_match_digits or not is_match_word:
        update.message.reply_text("Вы ввели неправильные данные")
        return

    first_addend = is_match_digits.group(1)
    operator = is_match_digits.group(2)
    second_addend = is_match_digits.group(3)
    try:
        result = operators_map[operator](int(first_addend), int(second_addend))
        update.message.reply_text(result)
    except ZeroDivisionError:
        update.message.reply_text("На ноль делить нельзя!!!")
        return


def play_in_cities(bot, update, args):

    cities = ['москва', 'артемьевск', 'калуга']
    if args:
        raw_input_city = args[0]
        if raw_input_city.lower() in cities:
            cities.remove(raw_input_city.lower())
        new_city_start_letter = raw_input_city[-1].lower()
        for city in cities:
            if city[0] == new_city_start_letter:
                update.message.reply_text(city)

'сколько будет три минус два'


def wordcount(bot, update, args):
    user_text = args
    if not user_text:
        update.message.reply_text("Пустая строка!!!!!!!!!!!!!!!")
    else:
        word_count = len(user_text)
        update.message.reply_text("Количество слов: {word_count}".format(word_count=word_count))


def tell_constellation(bot, update, args):

    date = '1970'

    planets = [ephem.Mars(date), ephem.Moon(date), ephem.Jupiter(date), ephem.Saturn(date)]
    if args:
        while len(planets) != 0:
            planet = planets.pop()
            if args[0].lower() == planet.name.lower():
                constel = ephem.constellation(planet)[1]
                update.message.reply_text(constel)
                return
        bot.sendMessage(update.message.chat_id, text="Не знаем такую планету")


def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
    print(update)


def show_error(bot, update, error):
    print(error)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


main()