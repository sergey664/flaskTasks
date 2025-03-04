from flask import Flask, url_for

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
