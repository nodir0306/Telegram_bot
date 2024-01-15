from googletrans import Translator
from bot import *
def translate_text_direction(message):
    if message.text == "Uzbek to English":
        bot.send_message(message.chat.id, "Enter the text you want to translate from Uzbek to English.")
        bot.register_next_step_handler(message, translate_text, dest_lang='en')
    elif message.text == "English to Uzbek":
        bot.send_message(message.chat.id, "Enter the text you want to translate from English to Uzbek.")
        bot.register_next_step_handler(message, translate_text, dest_lang='uz')
    elif message.text == "Back":
        startFunc(message)
    else:
        bot.send_message(message.chat.id, "Invalid selection. Please try again.")
        request_translation(message)

def translate_text(message, dest_lang):
    try:
        translation = translator.translate(message.text, dest=dest_lang)
        bot.send_message(message.chat.id, f"Original Text: {translation.origin}\nTranslated Text: {translation.text}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Translation failed. Error: {e}")
