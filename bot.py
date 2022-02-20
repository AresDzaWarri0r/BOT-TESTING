import os
import telegram
import random
from telegram import *
from telegram.ext import *

# Funciones
def handle_start(update, context):
    update.message.reply_text(
        text=(
            '◥█▀▀▀▀▀▀▀▀🔺▀▀▀▀▀▀▀▀█◤'
            '\n    ➖🅱️🅸🅴🅽🆅🅴🅽🅸🅳🅾️➖'
            '\n◢█▄▄▄▄▄▄▄▄🔻▄▄▄▄▄▄▄▄█◣'
            '\nUtiliza los Siguientes Comandos:'
            '\n/random - 🔀Genera un Número Aleatorio'
            '\n/myinfo - 👤 Muestra tu Información'
            '\n/reporte - ⤴️ Envía un mensaje a el Staff'
            '\n/prueba - ⛑ Aquí verás los comandos'
            '\nque se estén probando'
            '\n/hentai - 🔞'
            '\n/dp - 🧾 Revisa todos los Despachadores'
            
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Hola 👋🏻', callback_data='1')]
        ])
    )
    

def random_number(update, context):
    user_id=update.effective_user.id
    chat_id=update.message.chat.id
    number=random.randint(1,100)
    context.bot.sendMessage(chat_id= chat_id, parse_mode='Markdownv2', text=f"*╔◆❃◆╗*\n    # `*{number}*`\n*╚◆❃◆╝*")

def myinfo(update, context):
    user_id=update.effective_user.id
    name=update.effective_user.first_name
    last_name=update.effective_user.last_name
    username=update.effective_user.username
    is_bot=update.effective_user.is_bot
    context.bot.sendMessage(chat_id= user_id, parse_mode='Markdown', text=f"*🆔ID :* `{user_id}`\n*📛PRIMER NOMBRE :* `{name}`\n*📛APELLIDO :* `{last_name}`\n*🗞NOMBRE DE USUARIO :* `@{username}`\n*🤖ERES UN BOT:* `{is_bot}`\n*🔗ENLACE DE TELEGRAM :*\n [t.me/{username}](tg://user?id={user_id})")
    
def prueba(update, context):
    chat_id=update.message.chat.id
    user_id=update.effective_user.id
    context.bot.sendMessage(chat_id= chat_id, parse_mode='Markdownv2', text=f"_DE MOMENTO NO HAY NINGUNA_\n_FUNCIÓN EN_ *__PRUEBAS__* [⛑](tg://user?id={user_id})")
    #donde está puesto {user_id} cambiarlo por tu ID.
    
def hentai(update, context):
    username=update.effective_user.username
    user_id=update.effective_user.id
    chat_id=update.message.chat.id
    context.bot.sendMessage(chat_id= chat_id, text=f"Así te quería agarrar puerco 😈🔥, arderás en el caldero de Satán")
    context.bot.send_message(chat_id= chat_id, parse_mode='Markdownv2', text=f" [@{username}](tg://user?id={user_id}) Pillado usando /hentai en el bot 😂")
    #donde está chat_id= chat_id cambiar el 2do chat_id por el ID del grupo o canal donde quieran que vayan los mensajes.
    
def reporte(update, context):
    text=update.message.text
    username=update.effective_user.username
    name=update.effective_user.first_name
    chat_id=update.message.chat.id
    context.bot.sendMessage(chat_id= chat_id, parse_mode='Markdownv2', text=f"💬 {name} tu mensaje se ah *Enviado con Éxito ✅*")
    context.bot.send_message(chat_id= chat_id, parse_mode='Markdownv2', text=f"*Mensaje de : [@{username}](tg://user?id=1307228755)*\n`{text}`")
    #donde está chat_id= chat_id cambiar el 2do chat_id por el ID del grupo o canal donde quieran que vayan los mensajes.
    
def dp(update, context):
    user_id=update.effective_user.id
    chat_id=update.message.chat.id
    username=update.effective_user.username
    name=update.effective_user.first_name
    is_bot=update.effective_user.is_bot
    messageid=update.message.message_id
    last_name=update.effective_user.last_name
    context.bot.send_message(chat_id= chat_id, parse_mode='Markdownv2', text=f"*\nCommandHandler - start - handle_start\nCommandHandler - random - random_number\nCommandHandler - myinfo - myinfo\nCommandHandler - prueba - prueba\nCommandHandler - hentai - hentai\nCommandHandler - reporte - reporte\nCommandHandler - dp - dp*")

    
    # TOKEN
if __name__ == '__main__':
    token = os.environ['TOKEN']
    bot = telegram.Bot(token=token)
    updater = Updater(token=token, use_context=True)

    # Despachadores
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', handle_start))
    dp.add_handler(CommandHandler("random", random_number))
    dp.add_handler(CommandHandler("myinfo", myinfo))
    dp.add_handler(CommandHandler("prueba", prueba))
    dp.add_handler(CommandHandler("hentai", hentai))
    dp.add_handler(CommandHandler("reporte", reporte))
    dp.add_handler(CommandHandler("dp", dp))
    
    # Para Ejecutar el Bot
    updater.start_polling()
    print(f'running at @{bot.username}')
    updater.idle()
