#!/usr/bin/env python

import time
import json
import traceback
import sys
import logging
import os

from flask import Flask, request, session, jsonify, make_response, send_file, redirect, url_for, escape, abort
from flask_cors import CORS

from logging.handlers import RotatingFileHandler

from threading import Thread

from ORM import Project, User, Task
from playhouse.shortcuts import model_to_dict, dict_to_model
from datetime import datetime


app = Flask(__name__)
CORS(app)

##        #######   ######   #### ##    ## 
##       ##     ## ##    ##   ##  ###   ## 
##       ##     ## ##         ##  ####  ## 
##       ##     ## ##   ####  ##  ## ## ## 
##       ##     ## ##    ##   ##  ##  #### 
##       ##     ## ##    ##   ##  ##   ### 
########  #######   ######   #### ##    ## 

@app.route('/login', methods=['GET', 'POST'])  # POST:{username, password}
def login():
    if request.method == 'GET':
        return "Login Page" #render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        p = User.select().where(User.username == username)
        if len(p)==0:
            return make_error_message("No such user")
        elif len(p)==1:
            user = p[0]
            return login_check(user, username, password)
        else:
            return make_error_message("Too many users: " + username)

def login_check(user, username, password):
    if user.password == password:
        session['username'] = username
        return login_success(user)
    else:
        return make_error_message("Wrong password")

def login_success(user):    
    res = server_response()
    res['success'] = True
    res['user'] = model_to_dict(user)
    return jsonify(res)

def make_error_message(message):    
    res = server_response()
    res['success'] = False
    res['msg'] = message
    return jsonify(res)

def check_authentication():
    name = session.get("username", False)
    if not name:
        abort(401)    

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# test method
@app.route('/test')
def test():    
    return "yes , you are allowed"

########  ########  ######   ####  ######  ######## ######## ########  
##     ## ##       ##    ##   ##  ##    ##    ##    ##       ##     ## 
##     ## ##       ##         ##  ##          ##    ##       ##     ## 
########  ######   ##   ####  ##   ######     ##    ######   ########  
##   ##   ##       ##    ##   ##        ##    ##    ##       ##   ##   
##    ##  ##       ##    ##   ##  ##    ##    ##    ##       ##    ##  
##     ## ########  ######   ####  ######     ##    ######## ##     ## 

@app.route('/register', methods=['GET', 'POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    print 'register Header: %s\nusername: %s, password:%s'% (request.headers, username, password)
    if username <> '' and password <> '':
        if User.select().where(User.username==username).first():
            return jsonify({
                'success': False,
                'server_time': time.time(),
                'msg': u'User name existed!'
            })           

        user = User(username=username, password=password)
        user.save()
        return jsonify({
            'success': True,
            'server_time': time.time(),
            'msg': ''
        })
    return jsonify({
        'success': False,
        'server_time': time.time(),
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
    check_authentication()

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
    check_authentication()

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
    check_authentication()

    res = []
    p = User.select().where(True)
    for x in p:
        res.append(model_to_dict(x))
    
    return app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )

def server_response():
    return {
        "server_time": time.time(),
        "success": False,
        "data": []
    }

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

    app.secret_key = os.urandom(12)
    app.run(port=5000, debug=True, host='0.0.0.0')
