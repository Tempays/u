from flask_wtf import FlaskForm
from wtforms.fields.simple import EmailField, PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Пароль', validators=[DataRequired()])
    password_again = PasswordField(label='Повторите Пароль', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField(label='Имя', validators=[DataRequired()])
    age = StringField(label='Возраст', validators=[DataRequired()])
    position = StringField(label='Должность', validators=[DataRequired()])
    specialty = StringField(label='Специализация', validators=[DataRequired()])
    address = StringField(label='Адрес', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class JobForm(FlaskForm):
    job = StringField('Название Работы', validators=[DataRequired()])
    team_leader = StringField('Глава команды', validators=[DataRequired()])
    work_size = StringField('Длительность работ', validators=[DataRequired()])
    collaborators = StringField('Совместно трудящиеся')
    is_finished = BooleanField('Работа окончена?')
    submit = SubmitField('Подтвердить')