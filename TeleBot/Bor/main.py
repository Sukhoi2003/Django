# import telebot

# # Botning tokeni
# TOKEN = "6476325742:AAG62cDDiQMDrkDvd6nsF9pR6QYkhCBmvcM"

# # Botni yaratish
# bot = telebot.TeleBot(TOKEN)

# # /start komandasiga javob berish
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, "Salom! Men botman.")

# # Botni ishga tushirish
# bot.polling()
import telebot

# Botning tokeni
TOKEN = "6476325742:AAG62cDDiQMDrkDvd6nsF9pR6QYkhCBmvcM"

# Botni yaratish
bot = telebot.TeleBot(TOKEN)
# /start komandasiga javob berish
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom!")

# Botni ishga tushirish
bot.polling()
