from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired, Email


class Form(FlaskForm):
    name = StringField("Логин: ", validators=[DataRequired()], render_kw={"placeholder": "Введите имя"})
    password = PasswordField("Пароль: ", validators=[DataRequired()], render_kw={"placeholder": "Введите пароль"})
    email = EmailField("Email: ", validators=[Email()], render_kw={"placeholder": "Введите вашу почту"})
    remember = BooleanField('Запомнить:', default='checked')
    submit = SubmitField("Отправить")

