from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    r = requests.get('http://localhost:5000/on')
    print(r.content)
    return 'hello world'


@app.route('/on')
def on():
    return 'on'

app.run('localhost')