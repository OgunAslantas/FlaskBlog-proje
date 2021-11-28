from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(min=2,max=20)]) #name alanı boş olamaz dedik.
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Kayıt Ol')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Giriş')

class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    subtitle = StringField('Subtitle', validators = [DataRequired()])
    post_text = TextAreaField('Post Text', validators = [DataRequired()])
    submit = SubmitField('Post Ekle')

class ContactForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired(),])
    email = StringField('Email Adress', validators = [DataRequired(),Email()])
    phone = StringField('Phone Number', validators = [DataRequired()])
    message = TextAreaField('Message', validators = [DataRequired()])
    submit = SubmitField('Gönder')
