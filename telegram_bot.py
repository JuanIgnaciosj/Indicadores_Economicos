from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = ''  # Aqui integrar el uso de dotenv para dejar mejor el codigo
BOT_USERNAME: Final = ''  # Aqui va el nombre de la wea


# Comands

# Este es el texto que recibe cuando comienzas a interactuar con el bot
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Este es el mensaje de inicio!')

# Este es el texto que recibe cuando comienzas a interactuar con el bot


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Aqui te puedo ayudar ')

# Estes es el texto que recibe cuando comienzas a interactuar con el bot


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Aqui puedes agregar las funciones que deben salir desde la API')

# Respones


# Aqui maneja las respuestas cuanto se recibe un mensaje
def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'Hey there!'
    if 'how are you' in processed:
        return 'I am good!'
    if 'I love Python!' in processed:
        return 'Me too!'
    return 'I do not understand what you  wrote...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id} in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

        print('Bot', response)
        await update.message.reply_text(response)


# Funcion que maneja los errores
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ = '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # COMMANDS
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    # Para añadir un nuevo comando a las respuestas del bot
    # app.add_handler(CommandHandler('custom', custom_command))

    # MESSAGES
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # ERRORS
    app.add_error_handler(error)

    # POLLS THE BOT
    print('Polling...')
    app.run_polling(poll_interval=3)
