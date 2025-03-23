from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def base():
    return '''Нужно ввести профессию в строке'''


@app.route('/<title>')
def prof(title):
    if "инженер" in title or "строитель" in title:
        title = 'engineer'
    else:
        title = 'scientist'
    return render_template('prof.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')