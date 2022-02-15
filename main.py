from key import TOKEN
from functions import *


def main():
    updater = Updater(
        token=TOKEN,
        use_context=True
    )
    dispatcher = updater.dispatcher
    dispatcher.add_handler(
        CommandHandler("echo", info)
    )

    dispatcher.add_handler(MessageHandler(Filters.text("place"), what_place))
    dispatcher.add_handler(MessageHandler(Filters.regex("cd"), cd))

    dispatcher.add_handler(
        MessageHandler(
            Filters.text, lambda update, context: update.message.reply_text(
                f"Имя: {update.message.from_user.first_name}"
                f"Текст: {update.message.text}"
            )
        )
    )
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
