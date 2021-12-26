from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# function to handle the /start command
def start(update, context):
    update.message.reply_text('Привет чел с новым годом тебя')
# function to handle the /help command
def help(update, context):
    update.message.reply_text('Можешь помочь перекопать огород')
# function to handle errors occured in the dispatcher
def error(update, context):
    update.message.reply_text('КАжется ты ошибся')
    # function to handle normal text
def text(update, context):
    text_received = update.message.text
    update.message.reply_text(f'did you said "{text_received}" ?')
def main():
    TOKEN = "5093454870:AAFqpCS8pVth9jUBxSTHBwt0Y_zmp9Pe6O4"
    # create the updater, that will automatically create also a dispatcher and a queue to
    # make them dialoge
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # create the updater, that will automatically create also a dispatcher and a queue to
    # make them dialoge
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))
    # add an handler for errors
    dispatcher.add_error_handler(error)
    # start your shiny new bot
    updater.start_polling()
    # run the bot until Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()