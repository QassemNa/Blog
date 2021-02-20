from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from flask2.models import User


class RegistirationForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Sign up')

    def validate_username(selfself, username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, Choose another one')

    def validate_email(selfself, email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken Please choose another one')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign up')


class UpdateAccountForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture',
                        validators= [FileAllowed(['jpg', 'png'], 'wrong format')])
    submit = SubmitField('Update')

    def validate_username(selfself, username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken, Choose another one')

    def validate_email(selfself, email):
        if email.data != current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken Please choose another one')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


    def validate_email(selfself, email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There Is No account with that email. you must register first')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Reset Password')