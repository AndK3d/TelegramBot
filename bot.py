import config
import telebot
from time import sleep


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, "Hi cutie))")
    bot.send_message(message.chat.id, "I'm busy right now, but you can watch my live cam on this site")
    bot.send_message(message.chat.id, "http://2track.info/FdKi")

if __name__ == '__main__':
	bot.polling(none_stop=True)