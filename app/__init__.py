from flask import Flask
import json


app = Flask(__name__)
app.config["SECRET_KEY"] = "skjdgfbjkjbsdhkvaknclkjhabflabchjbsdb"
app.debug = True

base = "base.html"
other_base = "other_base.html"
days_base = "days_base.html"

messages_file_route = "app/static/files/messages.txt"

errors = {
    "404": "Страница не найдена. Проверьте URL адрес.",
    "405": "Неразрешенный метод"
}


def users():
    with open("app/static/files/users.txt", "r", encoding="UTF-8") as file:
        return json.loads(file.read())


def new_user(user):
    list_users = users()
    list_users.append(user)
    with open("app/static/files/users.txt", "w", encoding="UTF-8") as file:
        file.write(json.dumps(list_users))


from . import views
