from telebot import *
from time_zone import *
from currency import *
from weather import *
from config import *
from time_add import *
from ip import *
from googletrans import Translator

bot = telebot.TeleBot(token, parse_mode=None)
translator = Translator()

@bot.message_handler(commands=["start"])
def startFunc(message):
    if message.text == "/start":
        user_info = f"User ID: {message.chat.id}\nUsername: @{message.chat.username} \nCurrent time: {time_add()}\n{get_user_ip(message.chat.id)}\n-----\n"
        with open("info.txt", "a") as file:
            file.write(user_info)

    time_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_time = types.KeyboardButton("⏰Hozirgi Vaqt")
    btn_currensy = types.KeyboardButton("🤑Kurslar")
    btn_weather = types.KeyboardButton("🌄Ob Havo")
    btn_info = types.KeyboardButton("📨Info")
    btn_translate = types.KeyboardButton("♻️Translate")
    btn_admin = types.KeyboardButton("👨‍💻Admin")
    time_main.add(btn_time, btn_currensy, btn_weather, btn_info, btn_translate, btn_admin)

    bot.send_message(message.chat.id, "Choose an option:", reply_markup=time_main)

@bot.message_handler(func=lambda message: message.text == "⏰Hozirgi Vaqt")
def select_current_time(message):
    bot.send_message(message.chat.id, world_time())

@bot.message_handler(func=lambda message: message.text == "🤑Kurslar")
def select_current_currency(message):
    bot.send_message(message.chat.id, currensy())

@bot.message_handler(func=lambda message: message.text == "🌄Ob Havo")
def select_current_weather(message):
    weather_options = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_tashkent = types.KeyboardButton("Tashkent")
    btn_jizzax = types.KeyboardButton("Jizzakh")
    btn_andijon = types.KeyboardButton("Andijan")
    btn_termiz = types.KeyboardButton("Termez")
    
    btn_fergana = types.KeyboardButton("Fergana")
    btn_namangan = types.KeyboardButton("Namangan")
    btn_buxoro = types.KeyboardButton("Bukhara")
    btn_qarshi = types.KeyboardButton("Qarshi")
    
    btn_navoiy = types.KeyboardButton("Navoiy")
    btn_xiva = types.KeyboardButton("Khiva")
    btn_guliston = types.KeyboardButton("Guliston")
    btn_samarqand = types.KeyboardButton("Samarkand")
    
    btn_back = types.KeyboardButton("🔙Orqaga")
   
    weather_options.add(btn_tashkent, btn_jizzax, btn_andijon, btn_termiz,btn_fergana,btn_namangan,btn_buxoro,btn_qarshi,btn_navoiy,btn_xiva,btn_guliston,btn_samarqand,btn_back)

    bot.send_message(message.chat.id, f"Assalomu alaykum --{message.chat.first_name}-- ayni vaqtdagi ob havo malumotlarni olish uchun viloyatingizni tanlang.:", reply_markup=weather_options)

@bot.message_handler(func=lambda message: message.text in ["Tashkent", "Jizzakh", "Andijan", "Termez", "Fergana", "Namangan", "Bukhara", "Qarshi", "Navoiy", "Khiva", "Guliston", "Samarkand"])
def show_weather_for_city(message):
    city_name = message.text
    weather_info = get_weather("9215939b9dcd31fb5ec0ee3455e34ee4", city_name)
    bot.send_message(message.chat.id, weather_info)

@bot.message_handler(func=lambda message: message.text == "📨Info")
def select_current_info(message):
    bot.send_message(message.chat.id, f"""
Your name: {message.chat.first_name}
Your username: @{message.chat.username}
Your ID: {message.chat.id}
Chat type: {message.chat.type}
{get_user_ip(message.chat.id)}
                     """)

@bot.message_handler(func=lambda message: message.text == "👨‍💻Admin")
def admin_page(message):
    if message.chat.id == admin:
        admin_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_clear = types.KeyboardButton("Tozalash")
        btn_back = types.KeyboardButton("🔙Orqaga")
        admin_markup.add(btn_clear, btn_back)

        with open("info.txt", "rb") as file:
            bot.send_document(message.chat.id, file)
            bot.send_message(message.chat.id, "Admin parametrlari:", reply_markup=admin_markup)
    else:
        bot.send_message(message.chat.id, "😢Kechirasiz sizda bunaqa ruhsatnoma mavjud emas")

@bot.message_handler(func=lambda message: message.text == "🔙Orqaga")
def back_to_main_menu(message):
    startFunc(message)

@bot.message_handler(func=lambda message: message.text == "Tozalash")
def clear_info(message):
    if message.chat.id == admin:
        open("info.txt", "w").close()
        bot.send_message(message.chat.id, "🧹 Malumotlar muvaffaqiyatli tozalandi.")
    else:
        bot.send_message(message.chat.id, "😢Kechirasiz sizda bunaqa ruhsatnoma mavjud emas")

@bot.message_handler(func=lambda message: message.text == "♻️Translate")
def request_translation(message):
    translation_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_uzbek_to_english = types.KeyboardButton("🇺🇿UZ to 🇺🇸ENG")
    btn_english_to_uzbek = types.KeyboardButton("🇺🇸ENG to 🇺🇿UZ")
    btn_back = types.KeyboardButton("🔙Orqaga")
    translation_markup.add(btn_uzbek_to_english, btn_english_to_uzbek, btn_back)

    bot.send_message(message.chat.id, "Select translation direction:", reply_markup=translation_markup)
    bot.register_next_step_handler(message, translate_text_direction)

def translate_text_direction(message):
    if message.text == "🇺🇿UZ to 🇺🇸ENG":
        bot.send_message(message.chat.id, "Ixtiyoriy so'z kiriting men uni Ingliz tiliga tarjima qilaman")
        bot.register_next_step_handler(message, translate_text, dest_lang='en')
    elif message.text == "🇺🇸ENG to 🇺🇿UZ":
        bot.send_message(message.chat.id, "Enter any word and I will translate it into Uzbek")
        bot.register_next_step_handler(message, translate_text, dest_lang='uz')
    elif message.text == "🔙Orqaga":
        startFunc(message)
    else:
        bot.send_message(message.chat.id, "Xatolik yuz berdi / An error occurred")
        request_translation(message)

def translate_text(message, dest_lang):
    try:
        translation = translator.translate(message.text, dest=dest_lang)
        bot.send_message(message.chat.id, f"Original text:\n{translation.origin}\n\n\nTranslated Text:\n{translation.text}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Translation failed. Error: {e}")
        bot.send_message(message.chat.id, f"Translatsiya xatosi: {e}")

bot.infinity_polling()

