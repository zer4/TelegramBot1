import telebot

bot = telebot.TeleBot('5689002703:AAGb8pGpn-KW8_cyNNlSRMaNobcCbSgGZm4', parse_mode='Markdown')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '_Hello!_')

bot.polling()