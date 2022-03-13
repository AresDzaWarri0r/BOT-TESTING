import telegram
import os
import random
from telegram import *
from telegram.ext import *

INPUT_ANONIMO = 0
INPUT_REPORTE = 0
INPUT_DEAUTORIZAR = 0
INPUT_INFORME = 0
INPUT_PHOTO = 0


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

def autorizar(update, context):
    id=update.effective_user.id
    nombre=update.effective_user.first_name
    chat_id=update.message.chat.id
    context.bot.sendChatAction(chat_id=chat_id, action='upload_document', timeout=None)
    with open(f"{id}Autorización.txt", 'w') as f:
        f.write(f"{nombre}")
    context.bot.sendChatAction(chat_id=chat_id, action='typing', timeout=None)
    update.message.reply_text(parse_mode='MarkdownV2', text=f"*{nombre}* _tus datos han sido Guardados y Has sido autorizado_\n ID : `{id}` NOMBRE : `{nombre}`")
    print(f"AUTORIZACION :\nID : {id} NOMBRE : {nombre}")
def deautorizar(update, context):
    user_id=update.effective_user.id
    with open(f'{user_id}Autorización.txt', 'rb') as reader: autorizacion=reader.read()
    update.message.reply_text("Manda el ID del Usuario que quieras revocar su autorización..")
    return INPUT_DEAUTORIZAR
def delauth(update, context):
    chat_id=update.message.chat.id
    name=update.effective_user.first_name
    del_auth=f"{update.message.text}Autorización.txt"
    with open(f'{update.message.text}Autorización.txt', 'rb') as reader: delname=reader.read()
    context.bot.sendChatAction(chat_id=chat_id, action='typing', timeout=None)
    context.bot.sendMessage(chat_id=chat_id, text=f"{name} has desautorizado a {delname}".replace("b'", "").replace("'", "").replace("b"", "").replace(""", ""))
    os.unlink(del_auth)
    print(f"AUTORIZACION :\nID : {id} NOMBRE : {update.effective_user.first_name}")
    return ConversationHandler.END

def informe(update, context):
    user_id=update.effective_user.id
    with open(f'{user_id}Autorización.txt', 'rb') as reader: autorizacion=reader.read()
    update.message.reply_text('Que desesas Informar?')
    return INPUT_INFORME
def input_informe(update, context):
    chat_id=update.message.chat.id
    context.bot.sendMessage(chat_id='-1001363984343',parse_mode='Markdown',text=f"""
➖➖ Informe : {update.message.date} ➖➖
{update.message.text}
➖➖ Informe : {update.message.date} ➖➖
    """)
    update.message.pinned_message
    context.bot.sendMessage(chat_id=chat_id, parse_mode="MarkdownV2", text=f"Informe Realizado Con Éxito")
    return ConversationHandler.END

def t(update, context):
    text=update.message.text
    context.bot.sendChatAction(chat_id='-1001363984343', action='typing', timeout=None)
    context.bot.sendMessage(chat_id='-1001363984343', parse_mode='HTML', text=f"{text}".replace("/t ", ""))

def photo(update, context):
    update.message.reply_text('Manda una Foto')
    return INPUT_PHOTO
def input_photo(update, context):
    context.bot.sendMessage(chat_id=update.message.chat.id, text=f"{update.message.photo[2].fileid}")
    return ConversationHandler.END

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
    dp.add_handler(CommandHandler("autorizar", autorizar))
    dp.add_handler(CommandHandler("t", t))
    dp.add_handler(ConversationHandler(entry_points=[CallbackQueryHandler(pattern='button_reporte', callback=reporte)], states={INPUT_REPORTE: [MessageHandler(Filters.text, input_reporte)]}, fallbacks=[]))
    dp.add_handler(ConversationHandler(entry_points=[CallbackQueryHandler(pattern='button_anonimo', callback=anonimo)], states={INPUT_ANONIMO: [MessageHandler(Filters.text, input_anonimo)]}, fallbacks=[]))
    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('deautorizar', deautorizar)],states={INPUT_DEAUTORIZAR: [MessageHandler(Filters.text, delauth)]},fallbacks=[]))
    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('informe', informe)],states={INPUT_INFORME: [MessageHandler(Filters.text, input_informe)]},fallbacks=[]))
    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('photo', photo)],states={INPUT_PHOTO: [MessageHandler(Filters.photo, input_photo)]},fallbacks=[]))

    # Para Ejecutar el Bot
    updater.start_polling()
    print(f'Ejecutando el bot @{bot.username}')
    updater.idle()
