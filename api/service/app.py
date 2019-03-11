from flask import Flask, Blueprint
from flask_cors import CORS
from flask.ext.login import (LoginManager, login_required, login_user,
                             logout_user, UserMixin)

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

from ORM import Project, User, Task
from playhouse.shortcuts import model_to_dict, dict_to_model
from datetime import datetime

app = Flask(__name__)
CORS(app)

# ============ Login
app.secret_key = 's3cr3t'
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
 
@login_manager.user_loader
def load_user(user_id):
    user = User.select().where(User.id==user_id)
    return user

# ============

auth = Blueprint('auth', __name__)

##        #######   ######   #### ##    ## 
##       ##     ## ##    ##   ##  ###   ## 
##       ##     ## ##         ##  ####  ## 
##       ##     ## ##   ####  ##  ## ## ## 
##       ##     ## ##    ##   ##  ##  #### 
##       ##     ## ##    ##   ##  ##   ### 
########  #######   ######   #### ##    ## 

@auth.route('/login', methods=['GET', 'POST'])  # POST:{username, password}
def login():
    if 
    username = request.form['username']
    password = request.form['password']
    user = User.select().where(User.username == username)
    if user.username == username:    
        login_user(user)
    else:
        return 'login failed!'


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return "logout page"

# test method
@app.route('/test')
@login_required
def test():
    return "yes , you are allowed"


@app.route('/register', methods=['GET', 'POST'])
def register():
    username = request.get_json()['username']
    password = request.get_json()['password']
    print 'register Header: %s\nusername: %s, password:%s'% (request.headers, username, password)
    if username <> '' and password <> '':
        if User.select().where(User.username==username).first():
             return jsonify({
            'status': 'failure',
            'msg': u'User name existed!'
            })           

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({
        'status': 'success',
        'msg': 'register OK, please login!'
        })
    return jsonify({
    'status': 'failure',
    'msg': 'register fail, check username and password.'
    })

# TODO: serve static

@app.route('/')
def redirect_mobile():
    return None

   ###    ########  #### 
  ## ##   ##     ##  ##  
 ##   ##  ##     ##  ##  
##     ## ########   ##  
######### ##         ##  
##     ## ##         ##  
##     ## ##        #### 

@app.route('/api/task', methods=['GET'])    # ?date=20190301&user=Mike
def task_search():
    res = []
    p = Task.select()

    date_str  = request.args.get('date', None)
    user  = request.args.get('user', None)

    if date_str is not None:
        d = datetime.strptime(date_str, "%Y%m%d").date()
        p = p.where(Task.date == d)

    if user is not None:
        print user
        p = p.where(Task.user_name==user)

    for x in p:
        x.date = str(x.date)
        res.append(model_to_dict(x))

    return app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )


@app.route('/api/task/<id>', methods=['DELETE'])
def task_delete(id):
    Task.delete().where(Task.id == id).execute()

@app.route('/api/task/<id>', methods=['PUT'])
def task_update(id):
    p = Task(
            user_name = request.form['user_name'], 
            project_name = request.form['project_name'], 
            date = request.form['date'],
            hours = request.form['hours'],
            desc = request.form['description']
        )
    p.id = id
    p.save()

@app.route('/api/task', methods=['POST'])
def task_new():
    p = Task(
            user_name = request.form['user_name'], 
            project_name = request.form['project_name'], 
            date = request.form['date'],
            hours = request.form['hours'],
            desc = request.form['description']
        )
    p.save()

@app.route('/api/project', methods=['GET'])
def project_list():
    res = []
    p = Project.select().where(True)
    for x in p:
        res.append(model_to_dict(x))
    
    # return make_response(jsonify(**res), 200)

    return app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )

@app.route('/api/user', methods=['GET'])
def user_list():
    res = []
    p = User.select().where(True)
    for x in p:
        res.append(model_to_dict(x))
    
    return app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )


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
        '/tmp/service.log', maxBytes=10000000, backupCount=10)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)


    # conn=MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306, charset='utf8')
    # conn.select_db('python')
    # cur=conn.cursor()
    # cur.close()

    app.register_blueprint(auth, url_prefix='/auth')
    app.run(port=5000, debug=True, host='0.0.0.0')

    # conn.close()
