from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password_repeat = PasswordField("Повторите пароль", validators=[DataRequired(), EqualTo('password', message="Пароли должны совпадать")])
    surname = StringField("Фамилия", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    age = IntegerField("Возраст", validators=[DataRequired()])
    position = StringField("Должность", validators=[DataRequired()])
    speciality = StringField("Специальность", validators=[DataRequired()])
    address = StringField("Адрес", validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться")