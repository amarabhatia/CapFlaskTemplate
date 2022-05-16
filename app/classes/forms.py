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
    likeread = SelectField('Do you like to read?',choices=[(1,"yes"),(2,"sort of"),(3,"no")])
    genre = SelectField('Which Genre do you enjoy?',choices=[(1,"Non-Fiction"),(2,"Fiction"),(3,"None"),(1, "Horror"),(2,"Romance"),(1,"Bibliograhy")])
    sizebook = SelectField('How long of a book are you looking for?',choices=[(3,"100 Pages"),(2," 250 Pages"),(1,"300+ Pages")])
    movie = SelectField('Choose one of these movies you like the most:',choices=[(1,"Pulp Fiction"),(3, "Cloudy With a Chance of Meatballs"),(1, "The Godfather"),(2,"Anything Adam Sandler"),(3,"Willy Wonka and the Chocolate Factory")])
    favtrope = SelectField('Which is your favorite saying?',choices=[(1,"Kill two birds with one stone"),(2,"No pain no gain"),(3,"It's a peice of cake")])
    dreamv = SelectField('Where is your dream vacation?',choices=[(1,"Rome"),(1,"Italy"),(2, "France"), (2, "Tahiti"), (3, "Singapore"),(2, "Bora Bora"),(2,"Hawaii"),(3,"LA")])
    pickbook = SelectField('Would you pick up a book if it was not for school?',choices=[(1,"Yes"),(2, "Depends"), (2, "Sometimes"), (3, "Probably Not"),(3,"No,Never")])
    booksyear = SelectField('How many books do you read per year?',choices=[(3,"0"),(2, "1-5"), (1, "5+")])
    bookquote = SelectField('Which is your favorite book quote?',choices=[(3,"Love is or it ain't. Thin love ain't love at all."),(2, "I am not afraid of storms, for I am learning how to sail my ship."), (1, "It's the possibility of having a dream come true that makes life interesting."),(3,"What's the point of having a voice if you're gonna be silent in those moments you shouldn't be?")])
    submit = SubmitField('Post')