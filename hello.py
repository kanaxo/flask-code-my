from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    # return "Hello world"
    return render_template("index.html")

@app.route('/name/<name>')
def user(name):
    return render_template("name.html", user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
