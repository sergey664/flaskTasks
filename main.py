from flask import Flask

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def planet(planet_name="Сатурн"):
    name = planet_name.lower()
    if name == "марс":
        result = ["Эта планета близка к Земле",
                  "На ней много необходимых ресурсов",
                  "На ней есть вода и атмосфера",
                  "На ней есть небольшое магнитное поле",
                  "Наконец, она просто красива!"]
    elif name == "венера":
        result = ["Эта планета далеко от Земле",
                  "На ней нет необходимых ресурсов",
                  "На ней нет воды и атмосферы",
                  "На ней есть большое магнитное поле",
                  "Она некрасива!"]
    elif name == "сатурн":
        result = ["Эта планета на среднем расстоянии от Земли",
                  "На ней есть нужные ресурсы",
                  "Есть немного воды и воздуха",
                  "Среднее магнитное поле",
                  "Она красивая!"]
    return """<!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
        <title>реклама</title>
    </head>
    <body>
    <h1>Моё предложение: {}</h1>
    <h2>{}</h2>
    <div class="alert alert-primary" role="alert">
        <h3>{}</h3>
    </div>
    <div class="alert alert-info" role="alert">
        <h3>{}</h3>
    </div>
    <div class="alert alert-success" role="alert">
        <h3>{}</h3>
    </div>
    <div class="alert alert-warning" role="alert">
        <h3>{}</h3>
    </div>
    </body>
    </html>""".format(planet_name, *result)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    # http://127.0.0.1:8080/
