import
from flask import Flask, render_template , request , redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home', methods=['POST' , 'GET'])
def home():
    Full_name = request.form['Full_name']
    Email = request.form['Email']
    password = request.form['password']
    return render_template('home.html' , Full_name=Full_name , Email=Email , password=password)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
