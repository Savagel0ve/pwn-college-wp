from flask import Flask, redirect, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


app.run("hacker.localhost",8000)
