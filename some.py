from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import string


def palindrome(text):
    text = text.lower()

    cleaned = ''
    for char in text:
        if char.isalnum() or char in string.punctuation:
            cleaned += char

    reversed_text = cleaned[::-1]
    
    return cleaned == reversed_text, reversed_text


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Please send me a word or sentence, and I'll check if it's a palindrome.")


async def check_palindrome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    result, reversed_text = palindrome(text)

    if result:
        await update.message.reply_text(f"{reversed_text} matches {text} \n✅ It's a palindrome!")
    else:
        await update.message.reply_text(f"{reversed_text} does not match {text} \n❌ Not a palindrome.")

def main():
    bot_token = "7592457873:AAEFFNDOVQWcRZ6bJQCisjSNkoGauHRXUAE"  
    app = Application.builder().token(bot_token).build()

   
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_palindrome))

    app.run_polling()

if __name__ == '__main__':
    main()
