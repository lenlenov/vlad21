from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, IntegerField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])

    surname = StringField('Фамилия', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])



    submit = SubmitField('Войти')