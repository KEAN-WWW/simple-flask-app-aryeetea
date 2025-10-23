from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello CPS3500!"

@app.route("/new_page")
def new_page():
    return "This is a New Page!"

@app.route("/show_html")
def show_html():
    return render_template("hello.html")

@app.route("/user/<username>")
def user(username):
    return render_template("hello.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)