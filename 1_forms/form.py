from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
# secret key for csrf protection

app.config['SECRET_KEY'] = 'Your secret key'


class RegistrationForm(FlaskForm):
    """Form class for user registeration

    Attributes:
        Username stringField for username input
        Email: emailField for email input amd valodation
        submit : submitField to register a new user
    """


    username = StringField('username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')


@app.route("/register", methods=["GET", "POST"])
def register():    
        """This route handles registeration, submusion and validations

        Methods:
        GET : Displays the registeration form
        POST: proscess the validation and submits data
        """
        form = RegistrationForm()
    
    if form.validate_on_submit():
        # access form data with form.field.data
         username = form.username.data
         email = form.email.data

        # this iswhere you would normarly save ro database
        flash(f"Account created for {username}")
        # return("Registeration Successful")

    return render_template("register.html", form=form )

if __name__ == "__main__":
    app.run(debug=True)