from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, \
    PasswordField, EmailField, BooleanField, \
    SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, StopValidation, Length


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
    def validate_number_len(self, field):
        if "+7" not in field.data and len(field.data):
            raise ValidationError("Неверный номер")

    def validate_number_digits(self, field):
        if not field.data[1:].isdigit():
            raise ValidationError("Доступны только цифры")

    username = StringField("Никнейм: *", validators=[DataRequired()], render_kw={"placeholder": "Введите никнейм"})
    password = PasswordField("Пароль: *", validators=[DataRequired(), Length(min=4)], render_kw={"placeholder": "Введите пароль"})

    name = StringField("Имя: *", validators=[DataRequired()], render_kw={"placeholder": "Введите имя"})
    lastname = StringField("Фамилия: ", validators=[DataRequired()], render_kw={"placeholder": "Введите фамилию"})

    email = EmailField("Email: ", validators=[Email()], render_kw={"placeholder": "your@ema.il"})
    number = StringField("Телефон: ", validators=[validate_number_len, validate_number_digits],
                         render_kw={"placeholder": "+7XXXXXXXXXX"})

    submit = SubmitField("Отправить")

