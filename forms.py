from flask_wtf import FlaskForm
from wtforms import(
        StringField,
        PasswordField,
        SubmitField,
        IntegerField
        )
from wtforms.validators import(
        DataRequired,
        Email,
        EqualTo,
        Length,
        NumberRange
        )


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), 
        Length(min=2, max=20, message="Username must be between 2 and 20 characters.")
    ])
    email = StringField('Email', validators=[
        DataRequired(), 
        Email(message="Please enter a valid email address.")
    ])
    phone = StringField(
            'Phone',
            validators=[
                DataRequired(),
                Length(min=10, max=13, message="Please Enter a valid phone number")
                ]
            )
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6, message="Password should be at least 6 characters long.")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), 
        EqualTo('password', message="Passwords must match.")
    ])

"""
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
            'Confirm Password',
            validators=[DataRequired(), EqualTo('password')]
            )
    submit = SubmitField('Sign Up')
"""

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(), 
        Email(message="Please enter a valid email address.")
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class HirePurchaseForm(FlaskForm):
    months = IntegerField(
            'Number of Months',
            validators=[
                DataRequired(),
                NumberRange(min=1, max=24)
                ]
            )
    submit = SubmitField('Confirm Hire Purchase')
