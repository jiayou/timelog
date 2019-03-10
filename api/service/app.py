from flask_cors import CORS
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from flask import send_file

import numpy as np
import time
import json
import traceback
import sys

import logging
from logging.handlers import RotatingFileHandler
from threading import Thread

import MySQLdb

app = Flask(__name__)
CORS(app)

# TODO: serve static

@app.route('/')
def redirect_mobile():
    return None

@app.route('/api/task/{user}/{date}', methods=['GET'])
def task_list():
    res = []
    response = make_response(jsonify(res), 200)
    return response

'''
@app.route('/api/task/{user}/{date}', methods=['GET'])
@app.route('/api/task', methods=['POST'])
@app.route('/api/task', methods=['PUT'])
@app.route('/api/task', methods=['DELETE'])

@app.route('/api/proj', methods=['GET'])
@app.route('/api/proj', methods=['POST'])
@app.route('/api/proj', methods=['PUT'])
@app.route('/api/proj', methods=['DELETE'])

@app.route('/api/user', methods=['GET'])
@app.route('/api/user', methods=['POST'])
@app.route('/api/user', methods=['PUT'])
@app.route('/api/user', methods=['DELETE'])

@app.route('/auth', methods=['POST'])
@app.route('/login', methods=['POST'])
@app.route('/signup', methods=['POST'])

@app.route('/api/stat/last30day/{user}', methods=['GET'])

'''

if __name__ == '__main__':

    handler = RotatingFileHandler(
        '/var/log/supervisor/service.log', maxBytes=10000000, backupCount=10)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)


    conn=MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306, charset='utf8')
    conn.select_db('python')
    cur=conn.cursor()
    cur.close()

    app.run(port=5000, debug=False, host='0.0.0.0')

    conn.close()
