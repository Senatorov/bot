import random
import telebot
from telebot import types

TOKEN = '878010416:AAHr2zdcA3GihVrt3qwLveTL7wz7vCdvyTM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_messages(message: types.Message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет')

        keyboard = types.ReplyKeyboardMarkup()
        key_yes = types.KeyboardButton('Привет')
        keyboard.add(key_yes)
        key_no = types.KeyboardButton('Пока')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, text='asnwer', reply_markup=keyboard)

bot.polling()
