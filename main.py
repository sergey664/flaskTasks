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
    return render_template("list_prof.html", list_type=list_type, professions=professions)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
