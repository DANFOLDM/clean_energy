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
        NumberRange
        )


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


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
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
