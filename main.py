from flask import Flask, request, url_for
from PIL import Image
import io

app = Flask(__name__)


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" href="static/style.css">
                                <title>Загрузка фото</title>
                            </head>
                            <body>
                                <center>
                                <h1>Загрузка фотографии</h1>
                                <h3>Для участия в миссии</h3>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div>
                                        <label for="photo">Выберите файл</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </body>
                        </html>'''
    elif request.method == 'POST':
        file = request.files['file']
        binary = file.read()
        image = Image.open(io.BytesIO(binary))
        image.resize((300, 300)).save('static/img.png')
        return f'''<!doctype html>
                                <html lang="en">
                                    <head>
                                        <meta charset="utf-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                        <link rel="stylesheet"
                                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                        crossorigin="anonymous">
                                        <link rel="stylesheet" href="static/style.css">
                                        <title>Загрузка фото</title>
                                    </head>
                                    <body>
                                        <center>
                                        <h1>Загрузка фотографии</h1>
                                        <h3>Для участия в миссии</h3>
                                        <form class="login_form" method="post" enctype="multipart/form-data">
                                            <div>
                                                <label for="photo">Выберите файл</label>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                                <img src="static/img.png" alt="загрузите фото">
                                            </div>
                                            <button type="submit" class="btn btn-primary">Отправить</button>
                                        </form>
                                        <h1>Фото отправлено</h1>
                                    </body>
                                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
