from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return "<h1> Миссия Колонизация Марса"


@app.route('/carousel')
def index():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Image Slider</title>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<div class="container mt-4">
    <h2 class="text-center">Mars Image Slider</h2>

    <div id="marsCarousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="1000">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="static/img/MARS.png" class="d-block w-100" alt="Mars Image 1">
            </div>
            <div class="carousel-item">
                <img src="static/img/MARS-2-7.png" class="d-block w-100" alt="Mars Image 2">
            </div>
        </div>

        <button class="carousel-control-prev" type="button" data-bs-target="#marsCarousel" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#marsCarousel" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>

        <div class="carousel-indicators">
            <button type="button" data-bs-target="#marsCarousel" data-bs-slide-to="0" class="active"></button>
            <button type="button" data-bs-target="#marsCarousel" data-bs-slide-to="1"></button>
        </div>
    </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
