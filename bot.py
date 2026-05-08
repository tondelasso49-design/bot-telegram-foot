import telebot
import random

TOKEN = "8675415847:AAGrTeh-Qd9ifMFSVnnrNbZNFw79-TYUgQE"

bot = telebot.TeleBot(TOKEN)

analyses = [
    "✅ Victoire domicile",
    "✅ Plus de 2.5 buts",
    "✅ Les deux équipes marquent",
    "✅ Double chance",
    "❌ Match trop risqué"
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "⚽ Bot Football IA actif ! Tape /analyse")

@bot.message_handler(commands=['analyse'])
def analyse(message):
    choix = random.choice(analyses)
    bot.reply_to(message, f"📊 Analyse IA :\n{choix}")

print("Bot lancé...")
bot.infinity_polling()
