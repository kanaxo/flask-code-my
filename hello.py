from flask import Flask, render_template, flash, request, redirect, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "hello"
# Add SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Add MySQL database "mysql://username:password@localhost/dbname"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/users'

# Initialize database
db = SQLAlchemy(app)

# Create Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # create string
    def __repr__(self):
        return '<Name %r>' %self.name

# To initialize db: run createdb.py

# form
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

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

# ADD
@app.route('/user/add', methods=['GET','POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ""
        form.email.data = ""
        flash("User addeded successfully!")

    our_users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html",
        name = name,
        form = form,
        our_users=our_users)

# UPDATE
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        try:
            db.session.commit()
            flash("User updated Successfully!")
            # return render_template("update.html", form=form, name_to_update=name_to_update)
            return redirect( url_for('add_user') )
        except:
            flash("There is a problem!")
            return render_template("update.html", form=form, name_to_update=name_to_update)
        
    if request.method == "GET":
        return render_template("update.html", form=form, name_to_update=name_to_update)



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
    
