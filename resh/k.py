from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
import os

from werkzeug.utils import secure_filename
from wtforms.fields.simple import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class PhotoForm(FlaskForm):
    photo = FileField('Загрузить фото', validators=[FileRequired()])


@app.route('/')
@app.route('/index')
def index():
    return 'None'


@app.route('/galery', methods=['GET', 'POST'])
def prof():
    form = PhotoForm()

    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        print(filename)
        f.save(os.path.join('static', 'images', filename))
        return redirect('/galery')
    images = [f for f in os.listdir('static/images')]
    return render_template('galery.html', images=images, form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')