import telegram
import os
import random
from telegram import *
from telegram.ext import *

INPUT_ANONIMO = 0
INPUT_REPORTE = 0


def start(update, context):
    context.bot.sendChatAction(chat_id=update.message.chat_id, action='typing', timeout=None)
    user_id=update.effective_user.id
    context.bot.sendMessage(chat_id=user_id, text=f"""
Hola {update.effective_user.first_name}, te doy la Bienvenida al bot @{bot.username}
🚨 REPORTAR : Para hacer un reporte de Error o Sugerir una Función
🕵️ ANONIMO : Envía un mensaje a un grupo sin mostrar tu identidad
📔 COMANDOS : Aquí estará un listado con todos los comandos
    """,
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="🚨 REPORTAR", callback_data="button_reporte"), InlineKeyboardButton(text="🕵️ ANONIMO", callback_data="button_anonimo")],
        [InlineKeyboardButton(text=f"📔 COMANDOS", callback_data="button_ocomandos")],
        [InlineKeyboardButton(text=f"🤖 {bot.first_name}", url=f"t.me/{bot.username}")]]))

def random_number(update, context):
    chat_id=update.message.chat.id
    number=random.randint(1,100)
    context.bot.sendMessage(chat_id= chat_id, text="{}".format(number).replace("0", "0️⃣").replace("1", "1️⃣").replace("2", "2️⃣").replace("3", "3️⃣").replace("4", "4️⃣").replace("5", "5️⃣").replace("6", "6️⃣").replace("7", "7️⃣").replace("8", "8️⃣").replace("9", "9️⃣"))

def anonimo(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(parse_mode='MarkdownV2',text=f"🕵️ Mándame lo que quieras decir de forma anónima")
    return INPUT_ANONIMO

def input_anonimo(update, context):
    chat_id=update.message.chat.id
    text=update.message.text
    context.bot.sendChatAction(chat_id='-1001363984343', action='typing', timeout=None)
    context.bot.sendMessage(chat_id='-1001363984343', text=f"🔏Mensaje Anónimo :\n{text}")
    context.bot.sendChatAction(chat_id=chat_id, action='typing', timeout=None)
    context.bot.sendMessage(chat_id=chat_id, text=f"🤫 tu mensaje anónimo ha sido enviado....")
    return ConversationHandler.END

def reporte(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(parse_mode='MarkdownV2',text=f"🚨 Envía tu reporte 🚨")
    return INPUT_REPORTE

def input_reporte(update, context):
    name=update.effective_user.first_name
    user=f"@{update.effective_user.username}"
    chat_id=update.message.chat.id
    text=update.message.text
    context.bot.sendChatAction(chat_id=chat_id, action='typing', timeout=None)
    context.bot.sendMessage(chat_id='-1001470814819', text=f"🚨 REPORTE DE :\n{name} -- {user}:\n{text}".replace(" -- @none", ""))
    context.bot.sendChatAction(chat_id=chat_id, action='typing', timeout=None)
    context.bot.sendMessage(chat_id=chat_id, text=f"💬 {name} tu reporte se ah Enviado con Éxito ✅")
    return ConversationHandler.END

def ocomandos(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(parse_mode='MarkdownV2',text=f"""
➖➖➖ COMANDOS ➖➖➖
/random 👉 Genera un número Random
➖➖➖ COMANDOS ➖➖➖
    """)

def t(update, context):
    text=update.message.text
    context.bot.sendChatAction(chat_id='-1001363984343', action='typing', timeout=None)
    context.bot.sendMessage(chat_id='-1001363984343', parse_mode='HTML', text=f"{text}".replace("/t ", ""))

def filtros(update, context):
    msg=update.message.text
    number=random.randint(1,3)
    chat_id=update.message.chat.id
    if ("Hola" == msg):
        if (number == 1):
            estado = f"{update.effective_user.first_name} Hola"
            update.message.reply_text(text=estado)
        if (number == 2):
            estado = f"{update.effective_user.first_name} Que vuelta"
            update.message.reply_text(text=estado)
        if (number == 3):
            estado = f"Ohayo {update.effective_user.first_name}-Sama"
            update.message.reply_text(text=estado)
    if ("Adiós" == msg):
        if (number == 1):
            estado = f"{update.effective_user.first_name} Adiós"
            update.message.reply_text(text=estado)
        if (number == 2):
            estado = f"{update.effective_user.first_name} Cuídate"
            update.message.reply_text(text=estado)
        if (number == 3):
            estado = f"{update.effective_user.first_name} Vete plp 😐"
            update.message.reply_text(text=estado)
    if ("Adios" == msg):
        if (number == 1):
            estado = f"{update.effective_user.first_name} Adiós"
            update.message.reply_text(text=estado)
        if (number == 2):
            estado = f"{update.effective_user.first_name} Cuídate"
            update.message.reply_text(text=estado)
        if (number == 3):
            estado = f"{update.effective_user.first_name} Vete plp 😐"
            update.message.reply_text(text=estado)
    if ("Puta" == msg):
        if (number == 1):
            estado = f"{update.effective_user.first_name} no me provoques más 😐"
            update.message.reply_text(text=estado)
        if (number == 2):
            estado = f"{update.effective_user.first_name} puta tu y tu madre 😈"
            update.message.reply_text(text=estado)
        if (number == 3):
            estado = f"{update.effective_user.first_name} vuelves a decir puta y te meto el toto en el sobaco 🤬"
            update.message.reply_text(text=estado)
    if ("Ayuda" == msg):
        estado = f"{update.effective_user.first_name} necesita ayuda, pobrecito"
        update.message.reply_text(text=estado)
    if ("ID" == msg):
        estado = f"Este es tu ID : `{update.effective_user.id}`"
        update.message.reply_text(parse_mode="MarkdownV2", text=estado)
    if ("Mencióname" == msg):
        update.message.reply_text(parse_mode="MarkdownV2", text=f"[{update.effective_user.first_name}](tg://user?id={update.effective_user.id})")
    if ("Mencioname" == msg):
        update.message.reply_text(parse_mode="MarkdownV2", text=f"[{update.effective_user.first_name}](tg://user?id={update.effective_user.id})")
    if ("mencioname" == msg):
        update.message.reply_text(parse_mode="MarkdownV2", text=f"[{update.effective_user.first_name}](tg://user?id={update.effective_user.id})")
    if ("mencióname" == msg):
        update.message.reply_text(parse_mode="MarkdownV2", text=f"[{update.effective_user.first_name}](tg://user?id={update.effective_user.id})")
    if ("F gigante" == msg):
        context.bot.sendMessage(chat_id=chat_id, text=f"FFFFFFF\nF\nFFF\nF")

        # TOKEN
if __name__ == '__main__':
    token = os.environ['TOKEN']
    bot = telegram.Bot(token=token)
    updater = Updater(token=token, use_context=True)

    # Despachadores
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler("random", random_number))
    dp.add_handler(CallbackQueryHandler(pattern='button_ocomandos', callback=ocomandos))
    dp.add_handler(CommandHandler("t", t))
    dp.add_handler(ConversationHandler(entry_points=[CallbackQueryHandler(pattern='button_reporte', callback=reporte)], states={INPUT_REPORTE: [MessageHandler(Filters.text, input_reporte)]}, fallbacks=[]))
    dp.add_handler(ConversationHandler(entry_points=[CallbackQueryHandler(pattern='button_anonimo', callback=anonimo)], states={INPUT_ANONIMO: [MessageHandler(Filters.text, input_anonimo)]}, fallbacks=[]))
    dp.add_handler(MessageHandler(filters=Filters.text, callback=filtros)) ##FILTROS##

    # Para Ejecutar el Bot
    updater.start_polling()
    print(f'Ejecutando el bot @{bot.username}')
    updater.idle()
