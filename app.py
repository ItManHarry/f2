from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hello/')
def hello():
    return '<h1>Hello Flask 2!</h2>'
@app.route('/index')
def index():
    return render_template('index.html',  title='Index', name='Harry')