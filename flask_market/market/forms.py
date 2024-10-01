from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import length, equal_to, email, data_required, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user: 
            raise ValidationError('username already exists !!')
        
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('email address already exists !!')


    username = StringField(label='User Name ', validators=[length(min=2,max=30), data_required()])
    email_address = StringField(label='Email', validators=[email(), data_required()])
    password1 = PasswordField(label='Password', validators=[length(min=2), data_required()])
    password2 = PasswordField(label='Confirm password', validators=[equal_to('password1'), data_required()])
    submit = SubmitField(label='Submit')
    

class LoginForm(FlaskForm):
    username = StringField(label='User name:', validators=[data_required()])
    password = StringField(label='password:', validators=[data_required()])
    submit = SubmitField(label='Login')
