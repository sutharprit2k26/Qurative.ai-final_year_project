from jinja2 import Template
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/aboutus')
def About():
    return render_template('aboutus.html')


@app.route('/dev')
def dev():
    return render_template('devTeam.html')

if __name__ == '__main__':
    app.run(debug=True)
