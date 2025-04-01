import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired


from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    position = sqlalchemy.Column(sqlalchemy.String)
    speciality = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)
    job = orm.relationship('Jobs', back_populates='leader')


class RegisterForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Пароль', validators=[DataRequired()])
    repeat_password = PasswordField(label='Повторите Пароль', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField(label='Имя', validators=[DataRequired()])
    age = StringField(label='Возраст', validators=[DataRequired()])
    position = StringField(label='Должность', validators=[DataRequired()])
    specialty = StringField(label='Специализация', validators=[DataRequired()])
    address = StringField(label='Адрес', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


