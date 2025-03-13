from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/<title>')
def index(title):
    return render_template("base.html", title=title)


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    professions = ["инженер-строитель", "пилот",
                   "строитель", "экзобиолог",
                   "врач", "штурман"]
    return render_template("list_prof.html", file="style.css", list_type=list_type, professions=professions)


@app.route('/auto_answer')
@app.route('/answer')
def auto_answer():
    data = {
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": "True"
    }
    return render_template("auto_answer.html", file="style1.css", data=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', file="style2.css", title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
