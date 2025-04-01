from flask import Flask, request, make_response, render_template, redirect
from data import db_session
from data.department import Department
from data.users import User, RegisterForm
from data.jobs import Jobs
from data.db_session import global_init, create_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route("/jobs_table")
def jobs():
    global_init('db/new.db')
    db_sess = create_session()
    jobs = db_sess.query(Jobs).all()

    return render_template('jobs.html', jobs=jobs)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/success')
def success():
    return 'Успешно'




if __name__ == '__main__':
    main()