import telebot, requests
from bs4 import BeautifulSoup
from telebot.types import Message

TOKEN = "836997197:AAFvCr4oePuitIZJ6-cKLXNufSfquho6nz8"
bot = telebot.TeleBot(TOKEN)
urlMover = 'https://mover.uz'
urlsrc = '/search?val='


def findFromMover(data):
    txt = ''
    for i in data:
        txt = txt + i + '+'
    html = requests.get(urlMover+urlsrc+txt)
    html = html.content
    soup = BeautifulSoup(html)
    data = soup.find('div', {"class": "video-list vertical"})
    data = data.find('div', {"class": "video s first"})
    x = data.find('a', {"class": "image"})

    return x['href'],x['title']


@bot.message_handler(func=lambda message: True, commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, Бот работает пока-что) Тебе повезло!')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_text_messages(message):
    if message.text == '/razrab':
        bot.send_message(message.chat.id, "Мой царь и бог это Нуриддин)")
    cmd = message.text.split()
    if cmd[0] == '/search':
        href, title = findFromMover(cmd[1:])
        bot.send_message(message.chat.id, title + '\n' + urlMover + href)

bot.polling()
