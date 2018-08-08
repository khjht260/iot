## coding=utf-8
import sys
print(sys.version)
import json

from flask import Flask, request, jsonify
from flask_cors import CORS

from moodle_handler import MoodleHandler 
from basketball_machine import activate
from utils import merge_two_dicts


app = Flask(__name__)
CORS(app)

WebHandler = MoodleHandler()

activate = app.route('/activate')(activate)


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