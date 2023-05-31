from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/index')
def index(): 
    return render_template('index.html')