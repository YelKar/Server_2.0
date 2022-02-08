from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired, Email


class Form(FlaskForm):
    name = StringField("Логин: *", validators=[DataRequired()], render_kw={"placeholder": "Введите имя"})
    password = PasswordField("Пароль: *", validators=[DataRequired()], render_kw={"placeholder": "Введите пароль"})
    email = EmailField("Email: ", validators=[Email()], render_kw={"placeholder": "Введите вашу почту"})
    remember = BooleanField('Запомнить', default='checked')
    submit = SubmitField("Отправить")


class LoginForm(FlaskForm):
    username = StringField("Логин: *", validators=[DataRequired()], render_kw={"placeholder": "Введите имя"})
    password = PasswordField("Пароль: *", validators=[DataRequired()], render_kw={"placeholder": "Введите пароль"})
    remember = BooleanField('Запомнить', default='checked')
    submit = SubmitField("Отправить")


class NewAccount(FlaskForm):
    nikname = StringField("Никнейм: *", validators=[DataRequired()], render_kw={"placeholder": "Введите никнейм"})
    password = PasswordField("Пароль: *", validators=[DataRequired()], render_kw={"placeholder": "Введите пароль"})

    name = StringField("Имя: *", validators=[DataRequired()], render_kw={"placeholder": "Введите имя"})
    lastname = StringField("Фамилия: ", validators=[DataRequired()], render_kw={"placeholder": "Введите имя"})

    email = EmailField("Email: ", validators=[Email()], render_kw={"placeholder": "Введите вашу почту"})
    number = EmailField("Телефон: ", validators=[Email()], render_kw={"placeholder": "Введите ваш номер телефона"})

