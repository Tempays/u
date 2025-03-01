from flask import Flask, request

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def selection():
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
                            <link rel="stylesheet" type="text/css" href="static/style.css" />
                            <title>Гаян</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="name" placeholder="Введите Имя" name="name">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите Фамилию" name="surname">
                                    <p>   </p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Ваше образование</label>
                                        <select class="form-control" id="education_selec" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее Неполное</option>
                                          <option>Среднее Специальное</option>
                                          <option>Среднее Полное</option>
                                          <option>Высшее</option>
                                          <option>Окабе Ринтаро</option>
                                        </select>
                                     </div>
                                     
                                     <div class="form-group">
                                        <label for="jobs">Какой профессией Вы обладаете?</label>
                                     </div>
                                     
                                     <div class="form-group">
                                        <input type="checkbox" id="eng-exp" name="job" value="yes">
                                        Инженер-исследователь
                                    </div>
                                    
                                    <div class="form-group">
                                        <input type="checkbox" id="rob" name="job" value="yes">
                                        Робототехник
                                    </div>
                                    
                                    <div class="form-group">
                                        <input type="checkbox" id="eng_build" name="job" value="yes">
                                        Инженер-строитель
                                    </div>
                                    
                                    <div class="form-group">
                                        <input type="checkbox" id="pil" name="job" value="yes">
                                        Пилот
                                    </div>
                                    
                                    <div class="form-group">
                                        <input type="checkbox" id="ff" name="job" value="yes">
                                        Окабе Ринтаро
                                    </div>
                                        
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    
                                    
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['education'])
        print(request.form['email'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
