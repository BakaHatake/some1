from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import random

token="7610705253:AAGVc7Yy-uhBRAq3IESkbDxh4rdhVzZ6OHo"
bot = telebot.TeleBot(token)  

games={}

@bot.message_handler(commands=['start'])
def start_game(message):
    chat_id = message.chat.id

    games[chat_id] = {
        'secret_number': random.randint(1, 20),
        'guesses_taken': 0
    }
    bot.reply_to(message, "I'm thinking of a number between 1 and 20. Try to guess it!, you have 6 attempts")

@bot.message_handler(func=lambda message:message.chat.id in games)
def handle_guess(message):
    chat_id=message.chat.id
    game=games[chat_id]
    try:
        guess=int(message.text)
        game['guesses_taken'] += 1
    except ValueError:
        bot.reply_to(message, "Please enter a valid number.")
        return

    if guess < game['secret_number']:
        bot.reply_to(message, f"Your guess is too low. You have {6 - game['guesses_taken']} guesses left.")      
    elif guess > game['secret_number']:
        bot.reply_to(message, f"Your guess is too high. You have {6 - game['guesses_taken']} guesses left.")   
    else:
        bot.reply_to(message, f"Good job! You guessed my number in {game['guesses_taken']} guesses! \nType 'play again' to start a new game.")
        del games[chat_id]
        return

    if game['guesses_taken'] == 6:
        bot.reply_to(message, f"Game over! The number was {game['secret_number']}.\nType 'play again!' to start a new game.")
        del games[chat_id]

@bot.message_handler(func=lambda message: message.text.lower()=="play again")
def play_again(message):
      chat_id=message.chat.id
      games[chat_id]={
            'secret_number':random.randint(1,20),
            'guesses_taken':0
      }
      bot.reply_to(message,"Alrught! I'm thinking of a number between 1 and 20. Try to guess it!, you have 6 attempts")
    

@bot.message_handler(func=lambda message: message.chat.id not in games)
def no_game_active(message):
    bot.reply_to(message,"type /start to start a new game")

bot.polling()
