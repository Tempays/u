
from flask import Flask

app = Flask(__name__)


@app.route('/index')
def muter():
    return 'И на Марсе будут яблоки цвести!'


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/promotion')
def promote():
    sentences = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                 'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся к СВОим!']
    return '</br>'.join(sentences)


@app.route('/promotion_image')
def image():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="static/style.css">
</head>
<body>
    <h1>Жди нас, Марс!</h1>'
    <img src="static/img.png" alt="картинки нет">
    <p class="bg-primary text-white p-3">Человечество вырастает из дерева.</p>
    <p class="bg-success text-white p-3">Человечеству мала одна планета.</p>
    <p class="bg-danger text-white p-3">Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p class="bg-warning text-dark p-3">И начнем с Марса!</p>
    <p class="bg-info text-white p-3">Присоединяйся к СВОим!</p>
</body>
</html>
    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
