import telebot
from telebot.types import Message

TOKEN = "400408075:AAHhDxhhmoAMFrSajhS8QQfQPQdL2keL3q8"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, Бот работает пока-что) Тебе повезло!')


bot.polling()