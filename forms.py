from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    submit = SubmitField('login')


class SignUpForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    submit = SubmitField('signup')


class BlogForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    content = StringField('content', validators=[DataRequired()])
    submit = SubmitField('Post')
