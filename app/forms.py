# Add any form classes for Flask-WTF here
from wtforms.validators import InputRequired
from wtforms.validators import DataRequired, Email
from flask import Flask
from wtforms import SubmitField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField,TextAreaField, IntegerField,DecimalField,SelectField,PasswordField
from werkzeug.utils import secure_filename



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    name = StringField('Name', validators=[InputRequired()])
    locat = StringField("Location", validators=[DataRequired()],name = "Location")
    bio = TextAreaField("Bio", validators=[DataRequired()],name="Bio")
    email = StringField("Email",validators=[Email(),DataRequired()],name="Email")
    photo = FileField(validators=[FileRequired(), FileAllowed(['png', 'jpg','jpeg'], "wrong format!")])
    

class CarForm(FlaskForm):
    make = StringField('make', validators=[InputRequired()])
    model = StringField('model', validators=[InputRequired()])
    colour = StringField('Colour', validators=[InputRequired()])
    transmission = StringField('transmission', validators=[InputRequired()])
    year = StringField('Year', validators=[InputRequired()])
    price = DecimalField("Price", validators=[DataRequired()],name="Price",places = 2)
    car_type = StringField("car_type", validators=[DataRequired()],name = "car_type")
    desc = TextAreaField("Description", validators=[DataRequired()],name="Description")
    photo = FileField(validators=[FileRequired(), FileAllowed(['png', 'jpg','jpeg'], "wrong format!")])
    
