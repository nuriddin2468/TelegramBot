import telebot
from telebot.types import Message

TOKEN = "836997197:AAFvCr4oePuitIZJ6-cKLXNufSfquho6nz8"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True, commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, Бот работает пока-что) Тебе повезло!')


bot.polling()
