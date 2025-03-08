from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return "<h1> Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "<h1> И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    result = ["Человечество вырастает из детства.",
              "Человечеству мала одна планета.",
              "Мы сделаем обитаемыми безжизненные пока планеты.",
              "И начнем с Марса!",
              "Присоединяйся!"]
    return """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>реклама</title>
</head>
<body>
    <h3>{}</h3>
    <h3>{}</h3>
    <h3>{}</h3>
    <h3>{}</h3>
    <h3>{}</h3>
</body>
</html>""".format(*result)


@app.route('/image_mars')
def image():
    url_img = url_for('static', filename="img/MARS.png")
    result = ["Жди нас, Марс!", url_img, "Вот она какая, красная планет"]
    return """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>{}</h1>
    <img src="{}">
    {}
</body>
</html>""".format(*result)


@app.route('/promotion_image')
def promotion_image():
    url_style = url_for('static', filename="css/style.css")
    url_img = url_for('static', filename="img/MARS.png")

    result = [url_style,
              "Жди нас, Марс!",
              url_img,
              "Человечество вырастает из детства.",
              "Человечеству мала одна планета.",
              "Мы сделаем обитаемыми безжизненные пока планеты.",
              "И начнем с Марса!",
              "Присоединяйся!"
              ]

    return """<!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{}"/>
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>{}</h1>
        <img src="{}">
        <div class="alert alert-primary" role="alert">
        <h3>{}</h3>
        </div>
        <div class="alert alert-secondary" role="alert">
        <h3>{}</h3>
        </div>
        <div class="alert alert-success" role="alert">
        <h3>{}</h3>
        </div>
        <div class="alert alert-danger" role="alert">
        <h3>{}</h3>
        </div>
        <div class="alert alert-warning" role="alert">
        <h3>{}</h3>
        </div>
    </body>
    </html>""".format(*result)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Анкета претендента</h1>
                                <h2>На участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" placeholder="Введите фамилию">
                                        <input type="text" class="form-control" placeholder="Введите имя">
                                        <p>&nbsp;</p>
                                        <input type="email" class="form-control" placeholder="Введите адрес почты">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                            </select>
                                         </div>
                                        <div class="form-group">
                                            <label for="form-check">Какие у вас есть профессии?</label>
                                            <div class="form-check">
                                              <input type="checkbox" class="form-check-input" name="1">
                                              <label class="form-check-label" for="1">
                                                Инженер-исследователь
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input type="checkbox" class="form-check-input" name="2">
                                              <label class="form-check-label" for="2">
                                                Пилот
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input type="checkbox" class="form-check-input" name="1">
                                              <label class="form-check-label" for="1">
                                                Строитель
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input type="checkbox" class="form-check-input" name="2">
                                              <label class="form-check-label" for="2">
                                                Экзобиолог
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input type="checkbox" class="form-check-input" name="1">
                                              <label class="form-check-label" for="1">
                                                Врач
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input type="checkbox" class="form-check-input" name="2">
                                              <label class="form-check-label" for="2">
                                                Инженер по терраформированию
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input type="checkbox" class="form-check-input" name="1">
                                              <label class="form-check-label" for="1">
                                                Климатолог
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input type="checkbox" class="form-check-input" name="2">
                                              <label class="form-check-label" for="2">
                                                Специалист по радиационной защите
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите участвовать в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    result = [nickname, str(level), str(rating)]

    return """<!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
            <title>Результаты</title>
        </head>
        <body>
            <h1>Результаты отбора</h1>
            <h3>Претендента на участие в миссии {}: </h3>
            <div class="alert alert-success" role="alert">
                <h3>Поздравляем! Ваш рейтинг после {} этапа отбора</h3>
            </div>
            <div class="alert alert-none" role="alert">
                <h3>Составляет {}!</h3>
            </div>
            <div class="alert alert-warning" role="alert">
                <h3>Желаем удачи!</h3>
            </div>
        </body>
        </html>""".format(*result)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
