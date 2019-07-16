import telebot, requests
from bs4 import BeautifulSoup
from telebot.types import Message

TOKEN = "836997197:AAFvCr4oePuitIZJ6-cKLXNufSfquho6nz8"
bot = telebot.TeleBot(TOKEN)
urlMover = 'https://mover.uz'
urlVideo = 'https://v.mover.uz'
urlsrc = '/search?val='

cat = {
    'anime': '19',
    'music': '5',
}


def getVideo(href):
    return urlVideo + href[6:-1] + '_h.mp4'


def findFromMover(data='', category=''):
    txt = ''
    for i in data:
        txt = txt + i + '+'
    html = requests.get(urlMover+urlsrc+txt + '&category=' + category)
    html = html.content
    soup = BeautifulSoup(html)
    data = soup.find('div', {"class": "video-list vertical"})
    data = data.find('div', {"class": "video s first"})
    x = data.find('a', {"class": "image"})
    href = x['href']
    href = getVideo(href)
    print(href)
    return href, x['title']


@bot.message_handler(func=lambda message: True, commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, Бот работает пока-что) Тебе повезло!')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_text_messages(message):
    if message.text == '/razrab':
        bot.send_message(message.chat.id, "Мой царь и бог это Нуриддин)")
    cmd = message.text.split()
    if cmd[0] == '/anime':
        try:
            href, title = findFromMover(cmd[1:], cat['anime'])
            if title:
                bot.send_message(message.chat.id, title + '\n' + href)
        except Exception:
                bot.send_message(message.chat.id, 'Anime not found!')
    elif cmd[0] == '/music':
        try:
            href, title = findFromMover(cmd[1:], cat['music'])
            if title:
                bot.send_message(message.chat.id, title + '\n' + urlMover + href)
        except Exception:
            bot.send_message(message.chat.id, 'Music not found!')


bot.polling()
