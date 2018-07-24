from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators,FileField





class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=2, max=25)])
    # email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=2, max=25),validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

class UploadForm(FlaskForm):
    file=FileField('File Name',[validators.DataRequired()])