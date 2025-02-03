
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/nhs')
def nhs():
    return render_template("nhs.html")

@app.route('/charities')
def charities():
    return render_template("charities.html")

@app.route('/community')
def community():
    return render_template("community.html")


@app.route('/send')
def send():
    return render_template("send.html")
