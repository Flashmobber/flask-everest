from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return "About me"


@app.route("/user")
def user():
    return "User page"


if __name__ == '__main__':
    app.run()
