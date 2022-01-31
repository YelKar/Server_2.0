from flask import render_template, request, flash, redirect
from app import app, base, other_base,\
    messages_file_route, users, new_user
import json


# Messenger
with open(messages_file_route, "r", encoding="UTF-8") as messages_file:
    messages = json.loads(
        messages_file.read()
    )["messages"]


@app.route("/messenger")
def messenger():
    return render_template("messenger.html", base=other_base)


@app.route('/messenger/get_messages', methods=['GET'])
def get_messages():
    with open(messages_file_route, "r", encoding="UTF-8") as messages_file:
        messages = json.loads(
            messages_file.read()
        )["messages"]
    return {
        "messages": messages
    }


@app.route('/messenger/send_messages', methods=["GET", "POST"])
def send_messages():
    with open(messages_file_route, "r", encoding="UTF-8") as messages_file:
        messages = json.loads(messages_file.read())["messages"]
    req = request.json
    print(f"get_message{'_' * 49}")
    for key, val in req.items():
        print(f"{key}: {val}")
    print("_" * 60)
    if req["text"] == "clear":
        messages = [{"username": "Елисей", "text": "Привет", "timestamp": 1642944782.0538435}]
    else:
        messages.append(req)
    with open(messages_file_route, "w", encoding="UTF-8") as messages_file:
        messages_file.write(str({
            "messages": messages
        }).replace("'", '"'))
    return {
        "status": "OK",
    }

# Form
@app.route("/new_account", methods=["GET", "POST"])
def new_account():
    if request.method == "POST":
        get_form = dict(request.form)

        is_valid = {
            "is_username": get_form["username"],
            "is_not_in_site": not any(
                map(
                    lambda user: get_form["username"] == user["username"], users()
                )
            ),
            "is_name": get_form["name"],
            "is_valid_name": get_form["name"].isalpha() or not get_form["name"],
            "is_email/tel": get_form["email"] or get_form["tel"],
#            "is_chosen": get_form.get("select", False)
        }

        flash_messages = {
            "is_username": "Введите имя пользователя",
            "is_not_in_site": "Такой никнейм уже есть",
            "is_name": "Введите имя",
            "is_valid_name": "Некорректное имя",
            "is_email/tel": "Введите номер телефона или почту",
#            "is_chosen": "Выберите один из вариантов"
        }

        if not all(is_valid.values()):
            flash("Сообщение не принято: ", category="error title")
            for mess, is_val in zip(flash_messages.values(), is_valid.values()):
                if not is_val:
                    flash(mess, category="error")

        else:
            flash("Сообщение принято", category="ok")
            get_form["is_admin"] = False
            print("Add")
            new_user(get_form)
        print("_" * 20)
        for name, value in get_form.items():
            print(f"{name}: {value}")
        print("_" * 20)

    return render_template("new_account.html", base=base, title="Авторизация")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        get_form = dict(request.form)
        for user in users():
            if get_form["username"] == user["username"]:
                if get_form["password"] == user["password"]:
                    return redirect(f"/profile/{user['username']}")
                else:
                    flash("Неверный пароль", category="error")
                    break
        else:
            flash("Неверный логин", category="error")

    return render_template("login.html", base=base)


@app.route('/profile/<string:username>')
def profile(username):
    return render_template("profile.html", user=username, base=base, title="Профиль")
