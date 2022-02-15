from time import strftime
from telegram import Update
from telegram.ext import MessageHandler, Filters, CommandHandler, Updater, CallbackContext
from time import ctime


# /info
def info(update, _):
    user = update.message.from_user
    text = update.message.text.replace("/echo ", "").replace("/echo", "")
    update.message.reply_text(
        text=f"""Имя: {user.first_name}
Текст сообщения: {text if text else None}
Время получения: {strftime("%H:%M:%S %d.%m.%Y")}"""
    )


# github
place = ["$"]


def what_place(update: Update, context: CallbackContext):
    global place
    update.message.reply_text(" / ".join(place))


def cd(update: Update, context: CallbackContext):
    to = update.message.text[3:]
    global place
    if to[0] == "$":
        place = [to]
    elif to[0:3] == "../":
        place = place[:-to.count("../")]
        place.append(to[to.rfind("../"):])
    else:
        place.append(to)

    place = list(filter(lambda x: x != "../", place))
    if not place:
        place = ["$"]

    what_place(update, context)



