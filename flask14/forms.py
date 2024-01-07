from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Candidate Name", validators=[
                       DataRequired("Please enter your name.")])
    email = StringField("Email", validators=[
        DataRequired("Please enter your email address."),
        Email("Please enter a valid email address.")
    ])
    submit = SubmitField("Submit")
