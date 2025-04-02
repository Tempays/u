from flask import Flask, request, make_response, render_template, redirect
from sqlalchemy.testing.suite.test_reflection import users

from data import db_session
from data.department import Department
from data.users import User
from forms import RegisterForm, LoginForm, JobForm
from data.jobs import Jobs
from data.db_session import global_init, create_session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
global_init('db/new.db')

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).filter(User.id == user_id).first()


def main():
    db_sess = create_session()
    app.run()


@app.route("/")
@app.route("/index")
@app.route("/change_job")
def jobs():
    db_sess = create_session()
    jobs = db_sess.query(Jobs).all()

    return render_template('jobs.html', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.specialty.data,
            address=form.address.data,
            email=form.email.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/add_job', methods=['GET', 'POST'])
@app.route('/job', methods=['GET', 'POST'])
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(
            job=form.job.data,
            team_leader=form.team_leader.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data)
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template("addjob.html", form=form, message='Adding a job')


@app.route('/change_job/<job_id>', methods=['GET', 'POST'])
def change_job(job_id):
    form = JobForm()
    db_sess = db_session.create_session()
    if form.validate_on_submit():
        job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
        job.job = form.job.data
        job.team_leader = form.team_leader.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finisged = form.is_finished.data
        db_sess.commit()
        return redirect('/')
    else:
        if db_sess.query(Jobs).filter(Jobs.id == job_id).first():
            job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
            if current_user.is_authenticated:
                if (job.leader.id == current_user.id) or (current_user.id == 1):
                    return render_template("addjob.html", form=form, message=f"Changing a job number {job_id}")
        return redirect('/add_job')


@app.route('/delete_job/<job_id>', methods=['GET', 'POST'])
def delete_job(job_id):
    db_sess = db_session.create_session()
    if db_sess.query(Jobs).filter(Jobs.id == job_id).first():
        job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
        if current_user.is_authenticated:
            if (job.leader.id == current_user.id) or (current_user.id == 1):
                db_sess.delete(db_sess.query(Jobs).filter(Jobs.id == job_id).first())
                db_sess.commit()
    return redirect('/')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()