from telebot import TeleBot


bot = TeleBot('6476325742:AAG62cDDiQMDrkDvd6nsF9pR6QYkhCBmvcM')

class TextMatchFilter(AdvancedCustomFilter):
    key = 'text'

    def check(self, message, text):
        return text == message.text