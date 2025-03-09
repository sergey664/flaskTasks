from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    name = ""
    html = """<!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{}"/>
            <title>реклама</title>
        </head>
        <body>
        <h1>Загрузка фотографии</h1>
        <h3>Для участия в миссии</h3>
        <form class="login_form" method="post" enctype="multipart/form-data">
            Приложите фотографию
            <input type="file" class="form-control-file" id="photo" name="file">
            <img src="{}" alt="здесь должна была быть картинка, но не нашлась">
            <button type="submit" class="btn btn-primary">Записаться</button>
        </form>
        </body>
        </html>"""
    if request.method == 'GET':
        return html.format(url_for('static', filename='css/style.css'),
                           url_for('static', filename=f"img/{name}"))
    elif request.method == 'POST':
        if "file" in request.files:
            file = request.files["file"]
            name = file.filename
            file.save(f"static/img/{name}")
            return html.format(url_for('static', filename='css/style.css'),
                               url_for('static', filename=f"img/{name}"))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    # http://127.0.0.1:8080/
