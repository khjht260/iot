## coding=utf-8
import sys
print(sys.version)
import json

from flask import Flask, request, jsonify
from flask_cors import CORS

from moodle_handler import MoodleHandler 
# from basketball_machine import activate
activate = None
from utils import merge_two_dicts


app = Flask(__name__)
CORS(app)

WebHandler = MoodleHandler()

if activate is not None:
    activate = app.route('/activate')(activate)

@app.route('/set_db', methods=['POST'])
def set_db():
    data = request.get_json()
    WebHandler.set_db(key=data['username'], val=data['set_num'])
    return "True"

@app.route('/checkAuth', methods=['POST'])
def checkAuth():
    data = request.get_json()
    if WebHandler.checkAuth(data):
        userInfo = WebHandler.getUserInfo(data)
        print(userInfo)
        return jsonify({"permission": True, **userInfo})
    else:
        return jsonify({"permission": False})

app.run('localhost')