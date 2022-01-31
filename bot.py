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
            '\n/reglamento - 📖Consulta el Reglamento del Juego'
            '\n/participantes - 👥Listado de Participantes con los Roles'
            '\n/informacion - ℹ️Información sobre el juego'
            '\n/random - 🎲Genera un Número Aleatorio'
            '\n/myinfo - 👤Muestra tu Información'
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='🆎 UNIRSE AL GRUPO', url='https://t.me/+u9lg5-LMuF41MzMx')]
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

def reglamento(update, context):
    update.message.reply_text("""❗️REGLAMENTO❗️

✅ NO SE PUEDE HABLAR FUERA DE TURNO : Cada vez que haga esto tendrá una advertencia . A las 5 advertencias perderá el derecho a hablar en el tribunal.
✅ NO PRESENTAR PRUEBAS FALSAS : Si se descubre que un abogado a presentado pruebas falsas para defender o para incriminar perderá la palabra y tendrá una advertencia.
✅ NO PERMITIDO EL LENGUAJE OBSENO : Esto también equivale a una Advertencia.
✅ NO PERMITIR LA FALTA DE RESPETO ENTRE ABOGADOS : Cuando ocurra una discusión entre los dos bandos de abogados sino se detienen con el primer regaño estarán advertidos los dos.""")

def participantes(update, context):
    update.message.reply_text("""👤PARTICIPANTES✔️
🧑‍🦽@Yuna_Kisaragi       🧑‍🦽@Dabi_x_Toga_Forever
🧑‍⚖️@AresDza                  🙍@L99rp
🙍@SuperSaiayan       🏃‍♂️@tengounhambredepi

🚨ROLES
🧑‍⚖️ Juez - (1/1)

🙍Abogados - (2/2)

🏃‍♂️ Acusado - (1/1)

🧑‍🦽Víctimas - (2/♾)
    
🐵Testigos y 🙊Cómplices""")
    
def informacion(update, context):
    update.message.reply_text("""💬INFORMACIÓN
ᕮᒪ ᒍᑌᕮGO ᗪᕮᒪ ᒍᑌIᑕIO
 🏃‍♂️ Acusado , 🧑‍🦽Víctimas , 🙍Abogados , 🧑‍⚖️ Juez , 🐵 Testigos , 🙊Cómplices
Estos son los Roles que se encuentran en el juego. La denuncia será escogida aleatoriamente.
Los abogados podrán hablar por turnos e incluso utilizar pruebas que logren hacer mientras que no se demuestre que sean falsas . Los acusados tienen que moderar bien como hablan ya que cualquier cosa que digan puede ser usada en su contra. Las Víctimas podrán pasar a ser acusados en cualquier momento ...""")

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
    dp.add_handler(CommandHandler("reglamento", reglamento))
    dp.add_handler(CommandHandler("informacion", informacion))
    dp.add_handler(CommandHandler("participantes", participantes))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("random", random_number))
    dp.add_handler(CommandHandler("myinfo", myinfo))
    
    # Para Ejecutar el Bot
    updater.start_polling()
    print(f'running at @{bot.username}')
    updater.idle()
