from flask import Flask, render_template, url_for

app = Flask(__name__)


dict_ = {'surname': 'Маркс', 'name': 'Карл', 'education': 'Нет', 'job': 'помещик', 'sex': 'вертолет',
         'motivation': 'захотел', 'stay': True}


@app.route('/')
@app.route('/index')
def index():
    return 'None'


@app.route('/answer')
@app.route('/auto_answer')
def prof():
    return render_template('auto_answer.html', dict_=dict_)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')