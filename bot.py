bot.py
import telebot

# Bu yerga tokeningizni yozing
TOKEN = "7700335885:AAEWds5qifsoHihDhAV-bI_Dm0aE92SkBR4"
bot = telebot.TeleBot(TOKEN)

# Admin ID (raqam bo'lishi kerak)
ADMIN_ID = 6621886487  

# /start komandasi
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Assalomu alaykum! Bot ishlayapti ✅")

# Oddiy matnlarga javob
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.chat.id == ADMIN_ID:
        bot.reply_to(message, f"Admin yozdi: {message.text}")
    else:
        bot.reply_to(message, f"Siz yozdingiz: {message.text}")

bot.polling()
