from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
