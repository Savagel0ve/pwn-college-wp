from flask import Flask, redirect, render_template, request


app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    print(request.json)
    return "hackked"


app.run("hacker.localhost",8000)
