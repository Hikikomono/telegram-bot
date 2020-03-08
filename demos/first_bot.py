import logging

from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, Dispatcher, MessageHandler, Filters

from config import load

api_token = load.load_telegram_token()
updater = Updater(token=api_token, use_context=True)
dispatcher = updater.dispatcher
dispatcher: Dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Gib bitte noch einmal /start ein um zu überprüfen ob eh alles passt")


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Message:[{}], Sender[{}, {}]'.format(update.message.text,
                                                                        update.effective_user.username,
                                                                        update.effective_user.id))

    print('Message:[{}], Sender[{}]'.format(update.message.text, update.effective_user.username))


def echo_sticker_id(update: Update, context: CallbackContext):
    context.bot.send_sticker(chat_id=update.effective_chat.id,
                             sticker='CAACAgIAAxkBAAO7XmJWiZVJopFVdivAo1LziANNYb4AAggAA8A2TxNvbCYL3hqbaRgE')
    print('Sticker Received')


def run():
    echo_sticker_id_handler = MessageHandler(Filters.sticker, echo_sticker_id)
    echo_handler = MessageHandler(Filters.text, echo)
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(echo_sticker_id_handler)

    updater.start_polling()


# run()
