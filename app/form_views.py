from flask import render_template, request, \
    flash, redirect, session, \
    url_for
from app import app, base, other_base,\
    messages_file_route, users, new_user
import json
from app.forms import *

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
@app.route("/new_account", methods=["POST", "GET"])
def new_account():
    form = NewAccount()
    print(form.form_errors, form.number.errors)
    if form.validate_on_submit():
        print(form)
        json_form = {
            "username": form.username.data,
            "password": form.password.data,
            "name": form.name.data,
            "lastname": form.lastname.data,
            "email": form.email.data,
            "number": form.number.data
        }
        is_valid = {
            "is_username": form.username.data,
            "is_not_in_site": not any(
                map(
                    lambda user: form.username.data == user["username"], users()
                )
            ),
            "is_name": form.name.data,
            "is_valid_name": form.name.data.isalpha() or not form.name.data,
            "is_email/tel": form.email.data or form.number.data
        }

        flash_messages = {
            "is_username": "Введите имя пользователя",
            "is_not_in_site": "Такой никнейм уже есть",
            "is_name": "Введите имя",
            "is_valid_name": "Некорректное имя",
            "is_email/tel": "Введите номер телефона или почту"
        }

        if not all(is_valid.values()):
            flash("Сообщение не принято: ", category="error title")
            for mess, is_val in zip(flash_messages.values(), is_valid.values()):
                if not is_val:
                    flash(mess, category="error")

        else:
            flash("Сообщение принято", category="ok")
            json_form["is_admin"] = False
            print("Add")
            new_user(json_form)
        print("_" * 20)
        for name, value in json_form.items():
            print(f"{name}: {value}")
        print("_" * 20)

    return render_template("new_account.html", base=base, title="Авторизация", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    l_form = LoginForm()
    if form.validate_on_submit():
        print(l_form.username.data)
        print(l_form.password.data)
        for user in users():
            if l_form.username.data == user["username"]:
                if l_form.password.data == user["password"]:
                    return redirect(f"/profile/{user['username']}")
                else:
                    flash("Неверный пароль", category="error")
                    break
        else:
            flash("Неверный логин", category="error")
    return render_template("login.html", form=l_form, base=base)


@app.route('/form', methods=['GET', 'POST'])
def form():
    print("logged-in" in session)
    if "logged-in" in session:
        return redirect(url_for("profile", username=session["logged-in"]))

    if request.method == "POST":
        get_form = dict(request.form)
        for user in users():
            if get_form["username"] == user["username"]:
                if get_form["password"] == user["password"]:
                    session["logged-in"] = user["username"]
                    return redirect(url_for("profile", username=user["username"]))
                else:
                    flash("Неверный пароль", category="error")
                    break
        else:
            flash("Неверный логин", category="error")

    return render_template("form.html", base=base)


@app.route('/profile/<string:username>')
def profile(username):
    return render_template("profile.html", user=username, base=base, title="Профиль")

