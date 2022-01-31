from app import app, \
    base, other_base, days_base
from flask import render_template, url_for


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", base=base,
                           title="Сайт начинающего верстальщика 2.0")


@app.route('/days')
def select_day():
    return render_template("days.html", base=days_base,
                           title="Список дней", )


@app.route('/day-<int:num>')
def days(num):
    return render_template(f"days/day-{num}.html", num=num, max=15, name="days",
                           base=days_base, title=f"День-{num}", body_pos="")


@app.route('/photo-<int:num>')
def photos(num):
    return render_template(f"days/photo-{num}.html", title=f"Фотографии. Страница {num}",
                           base=days_base, num=num, max=3, name="photos")


@app.route("/other")
def other():
    return render_template("other_pages/other_pages_links.html", base=other_base, title="Другие страницы сайта")


@app.errorhandler(404)
def not_found(e):
    print(e)
    return render_template("404.html", title="404", error=e, base=base)


# Ссылки на другие страницы
from . import other_views
from . import form_views
