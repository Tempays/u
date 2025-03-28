import random

from flask import Flask, render_template, url_for
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def random_filter(seq):
    return random.choice(seq)


def sorted_filter(seq):
    return ', '.join(sorted(seq))


app.jinja_env.filters['random'] = random_filter
app.jinja_env.filters['sort'] = sorted_filter


@app.route('/')
@app.route('/index')
def index():
    return 'None'


@app.route('/member')
def memeber():
    with open('templates/crew.json', encoding='utf8', mode='r') as file:
        list_ = json.load(file)
    return render_template('crew.html', crew=list_, title='crew')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')