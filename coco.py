from flask import Flask as flask
from flask import render_template, redirect, url_for, request

app = flask(__name__)


@app.route('/')
def home():
    return render_template('a.html')


if __name__ == "__main__":
    app.run(debug=True)

