import random
import telebot
from telebot.types import Message

TOKEN = '878010416:AAHr2zdcA3GihVrt3qwLveTL7wz7vCdvyTM'
bot = telebot.TeleBot(TOKEN)

smiles = ['😂','😘','❤','😊','😒','😳','😜','💋','😋','😆']

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message):
    bot.reply_to(message, 'Привет')

@bot.message_handler(func=lambda message: True)
def smile(message: Message):
    bot.reply_to(message, random.choice(smiles))



bot.polling()