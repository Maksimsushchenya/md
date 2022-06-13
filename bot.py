import config
import telebot
from pycbrf import ExchangeRates
from datetime import date
bot = telebot.TeleBot(config.TOKEN)
rates = ExchangeRates('2022-06-13')
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, "Привет! Я бот")
@bot.message_handler(commands=["help"])
def help(message):
	bot.send_message(message.chat.id, "Ничем не могу тебе помочь(")
@bot.message_handler(commands=["usd"])
def usd(message):
	text = "1 Доллар США ="+str(rates['USD'].rate)+"руб."
	bot.send_message(message.chat.id, text)
if __name__ == '__main__':
	bot.infinity_polling()