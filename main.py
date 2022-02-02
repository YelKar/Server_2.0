from time import ctime
from key import TOKEN
from functions import *


def main():
    updater = Updater(
        token=TOKEN,
        use_context=True
    )
    dispatcher = updater.dispatcher
    dispatcher.add_handler(
        CommandHandler("info", info)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.text("Привет"), say_hello)
    )
    dispatcher.add_handler(
        MessageHandler(
            Filters.text, lambda update, context: update.message.reply_text(update.message.text)
        )
    )
    updater.start_polling()
    print("Bot had been started")
    updater.idle()


if __name__ == '__main__':
    main()