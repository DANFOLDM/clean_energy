from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), 
        Length(min=2, max=20, message="Username must be between 2 and 20 characters.")
    ])
    email = StringField('Email', validators=[
        DataRequired(), 
        Email(message="Please enter a valid email address.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6, message="Password should be at least 6 characters long.")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), 
        EqualTo('password', message="Passwords must match.")
    ])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(), 
        Email(message="Please enter a valid email address.")
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
