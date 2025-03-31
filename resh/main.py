from flask import Flask, request, make_response, render_template
from data import db_session
from data.department import Department
from data.users import User
from data.jobs import Jobs
from data.db_session import global_init, create_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route("/jobs")
def jobs():
    global_init('db/new.db')
    db_sess = create_session()
    jobs = db_sess.query(Jobs).all()

    return render_template('jobs.html', jobs=jobs)



if __name__ == '__main__':
    main()