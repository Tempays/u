from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return 'None'


@app.route('/list_prof/<order>')
def prof(order):
    if order == 'ol' or order == 'ul':
        return render_template('prof.html', order=order)
    else:
        return '''Неверный аргумент'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')