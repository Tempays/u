from flask import Flask, url_for

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


@app.route('/image_mars')
def image():
    return '''<h1>Жди нас, Марс!</h1>'
            <img src="static/img.png" alt="картинки нет">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
