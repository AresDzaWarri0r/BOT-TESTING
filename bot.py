import os
import telegram
import random
from telegram import *
from telegram.ext import *

# Funciones
def handle_start(update, context):
    update.message.reply_text(
        text=(
            '❗️BIENVENIDO AL BOT...'
            '\nUtiliza los Sguientes Comandos:'
            '\n/random - 🎲Genera un Número Aleatorio'
            '\n/myinfo - 👤Muestra tu Información'
            
            
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='👾CÓDIGO FUENTE', url='https://github.com/AresDza/PRUEBAS/')]
        ])
    )
def about(update, context):

    update.message.reply_text(
        text=(
            '❗️BOT ALOJADO EN HEROKU'
            '\nCON REPOSITORIO EN GITHUB'
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='👾CÓDIGO FUENTE', url='https://github.com/AresDza/PRUEBAS/')]
        ])
    )

def random_number(update, context):
    user_id = update.effective_user['id']
    number = random.randint(0,20)
    context.bot.sendMessage(chat_id= user_id, parse_mode='Markdown', text=f"➖➖➖➖➖➖\n➡️*Número : #* `{number}`⬅️\n➖➖➖➖➖➖")

def myinfo(update, context):
    user_id = update.effective_user['id']
    name = update.effective_user['first_name']
    username = update.effective_user['username']
    last_name = update.effective_user['last_name']
    is_bot = update.effective_user['is_bot']
    context.bot.sendMessage(chat_id= user_id, parse_mode='Markdown', text=f"*🆔ID :* `{user_id}`\n*📛PRIMER NOMBRE :* `{name}`\n*📛APELLIDO :* `{last_name}`\n*🗞NOMBRE DE USUARIO :* `@{username}`\n*🤖ERES UN BOT:* `{is_bot}`\n*🔗ENLACE DE TELEGRAM :* \n↪️ t.me/{username}")

    # TOKEN
if __name__ == '__main__':
    token = os.environ['TOKEN']
    bot = telegram.Bot(token=token)
    updater = Updater(token=token, use_context=True)

    # Despachadores
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', handle_start))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("random", random_number))
    dp.add_handler(CommandHandler("myinfo", myinfo))
    
    # Para Ejecutar el Bot
    updater.start_polling()
    print(f'running at @{bot.username}')
    updater.idle()
