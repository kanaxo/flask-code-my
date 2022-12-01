from flask import Flask, render_template, flash

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "hello"

# form
class nameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')
def hello():
    # return "Hello world"
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = nameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Name submitted successfully!")

    return render_template("name.html",
        name = name,
        form = form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
