from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def index():
      a = {'name':'Suthiphong'}
      Res = json.dumps(a)
      return Res

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        return request.form['param1'] + request.form['param2']
    if request.method == 'GET':
        return "User GETDATA"
        

