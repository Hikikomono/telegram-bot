import logging

from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, Dispatcher, MessageHandler, Filters

updater = Updater(token='756295721:AAFPvKk8A0wSJ7RxBx2IzEsDHJ2BPc9GYS4', use_context=True)
dispatcher = updater.dispatcher
dispatcher: Dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Gib bitte noch einmal /start ein um zu überprüfen ob eh alles passt")


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Message:[{}], Sender[{}]'.format(update.message.text,
                                                                    update.effective_user.username))

    print('Message:[{}], Sender[{}]'.format(update.message.text, update.effective_user.username))


echo_handler = MessageHandler(Filters.text, echo)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()
