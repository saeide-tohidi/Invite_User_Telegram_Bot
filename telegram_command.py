import time
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application, filters, MessageHandler

TOKEN = "7308458820:AAHzEwmfvo1ojYTi4r5N5K4nMgYSDvQSZj4"
BOTUSERNAME = '@whitecherrypickbot'



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Start {update.effective_user.first_name}')


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')



def handle_response(text:str)-> str:
    response:str = text.lower()

    if 'hello' in response:
        return 'Hello your welcome'
    if 'how are you' in response:
        return 'I,m fine thank you'

    return 'I can not understand what you wrote!!'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text:str = update.message.text
    user:int = update.message.chat.id

    print(f"User {user} in {message_type}: {text}")


    if message_type == 'group':
        if BOTUSERNAME in text:
            new_text:str = text.replace(BOTUSERNAME, '').strip()
            response:str = handle_response(new_text)

        else:
            return

    else:
        response:str = handle_response(text)
    print("Bot: ", response)
    await update.message.reply_text(response)





async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == '__main__':
    print('start bot')

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('hello', hello_command))


    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    # Errors
    app.add_error_handler(error)
    app.run_polling(poll_interval=3)

