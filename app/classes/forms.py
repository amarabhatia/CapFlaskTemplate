# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask.app import Flask
from flask import flash
from flask_wtf import FlaskForm
from mongoengine.fields import EmailField
import mongoengine.errors
from wtforms.validators import URL, NumberRange, Email, Optional, InputRequired, ValidationError, DataRequired, EqualTo
from wtforms import PasswordField, StringField, SubmitField, TextAreaField, HiddenField, IntegerField, SelectField, FileField, BooleanField
from app.classes.data import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me?')
    submit = SubmitField()

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])  
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        try:
            User.objects.get(username=username.data)
        except mongoengine.errors.DoesNotExist:
            flash(f"{username.data} is available.")
        else:
            raise ValidationError('This username is taken.')

    def validate_email(self, email):
        try:
            User.objects.get(email=email.data)
        except mongoengine.errors.DoesNotExist:
            flash(f'{email.data} is a unique email address.')
        else:
            raise ValidationError('This email address is already in use. if you have forgotten your credentials you can try to recover your account.')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role',choices=[("Teacher","Teacher"),("Student","Student")]) 
    CorV = SelectField('Chocolate or Vanilla',choices=[("Chocolate","Chocolate"),("Vanilla","Vanilla")])



class PostForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Post', validators=[DataRequired()])
    submit = SubmitField('Post')
    readorno = SelectField('Do you read?',choices=[("Yes","Yes"),("No","No"),("Sort of","Sort of")])



class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class BookReviewForm(FlaskForm):
    # fname = StringField('First Name', validators=[DataRequired()])
    # lname = StringField('Last Name', validators=[DataRequired()])
    booktitle = StringField('Title of Novel:', validators=[DataRequired()]) 
    authorname = StringField('Author:', validators=[DataRequired()]) 
    rating = SelectField('How would you rate it out of five?',choices=[("1","1"),("1.5","1.5"),("2","2"),("2.5","2.5"),("3","3"),("3.5","3.5"),("4","4"),("4.5","4.5"),("5","5")])
    userthoughts = TextAreaField('What were your thoughts on the book?', validators=[DataRequired()]) 
    spoilers =  SelectField('Are there spoilers?',choices=[("yes","yes"),("no","no")])
    submit = SubmitField('Post')

class QuizForm(FlaskForm):
    likeread = SelectField('Do you like to read?',choices=[("yes","yes"),("sort of","sort of"),("it's complicated","it's complicated"),("no","no")])
    genre = SelectField('Which Genre do you enjoy??',choices=[("yes","yes"),("sort of","sort of"),("it's complicated","it's complicated"),("no","no")])
    submit = SubmitField('Post')