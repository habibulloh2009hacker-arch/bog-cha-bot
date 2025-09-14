
import telebot

# Bu yerga o'zingizning tokeningizni qo'ying
TOKEN = "7700335885:AAEWds5qifsoHihDhAV-bI_Dm0aE92SkBR4"
bot = telebot.TeleBot(TOKEN)

# Bu yerga o'zingizning Telegram IDingizni yozing
ADMIN_ID = 6621886487  

# Har bir foydalanuvchining ma'lumotlarini vaqtincha saqlash uchun
user_data = {}

# Savollar ro'yxati
questions = [
    "Ismingizni kiriting:",
    "Familiyangizni kiriting:",
    "Tug‘ilgan kuningizni kiriting (masalan: 12.05.2018):",
    "Yoshingizni kiriting:",
    "Telefon raqamingizni kiriting:",
    "Yashash manzilingizni kiriting:"
]

# Foydalanuvchi qaysi savolda ekanini kuzatish uchun
current_question = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    user_data[user_id] = []
    current_question[user_id] = 0
    bot.send_message(user_id, "Assalomu alaykum! Ro'yxatdan o'tish uchun savollarga javob bering.")
    bot.send_message(user_id, questions[0])

@bot.message_handler(func=lambda message: True)
def answer(message):
    user_id = message.chat.id

    # Agar foydalanuvchi /start bosmagan bo‘lsa
    if user_id not in current_question:
        bot.send_message(user_id, "Iltimos, /start tugmasini bosing.")
        return

    # Javobni saqlash
    user_data[user_id].append(message.text)

    # Keyingi savolga o'tish
    current_question[user_id] += 1

    if current_question[user_id] < len(questions):
        bot.send_message(user_id, questions[current_question[user_id]])
    else:
        # Barcha savollar tugadi
        bot.send_message(user_id, "✅ Siz muvaffaqiyatli ro'yxatdan o'tdingiz!")

        # Admin'ga xabar yuborish
        info = "\n".join(f"{questions[i]} {user_data[user_id][i]}" for i in range(len(questions)))
        bot.send_message(ADMIN_ID, f"📩 Yangi ro'yxatdan o'tish:\n\n{info}")

        # Ma'lumotlarni tozalash
        del current_question[user_id]
        del user_data[user_id]

# Botni doimiy ishlatish
bot.polling(none_stop=True)
