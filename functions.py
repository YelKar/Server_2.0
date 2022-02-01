from time import strftime


# /info
def info(update, _):
    user = update.message.from_user
    text = update.message.text.replace("/echo ", "").replace("/echo", "")
    update.message.reply_text(
        text=f"""Имя: {user.first_name}
Текст сообщения: {text if text else None}
Время получения: {strftime("%H:%M:%S %d.%m.%Y")}"""
    )
