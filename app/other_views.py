from flask import render_template
from app import app, base, other_base

@app.route("/clock")
def clock():
    return render_template("other_pages/time.html", title="Часы", base=other_base)


@app.route('/binaryClock')
def binClock():
    return render_template("other_pages/binClock.html", title="Бинарные часы", base=other_base)


@app.route("/games/dino")
def dino():
    return render_template("other_pages/dino.html", base=other_base, title="dino")


@app.route("/games/flappyBird")
def flappy_bird():
    return render_template("other_pages/flappyBird.html", base=other_base, title="FlappyBird")


@app.route("/detectClient")
def detect_client():
    return render_template("other_pages/detectClient.html", base=other_base, title="Определение операционной системы")