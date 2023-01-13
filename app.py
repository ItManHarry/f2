from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
@app.route('/hello/')
def hello():
    return '<h1>Hello Flask 2!</h2>'
@app.route('/index')
def index():
    return render_template('index.html',  title='Index', name='Harry')
@app.route('/')
def home():
    return redirect(url_for('index'))