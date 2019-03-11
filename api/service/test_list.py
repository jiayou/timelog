from ORM import Project, User, Task
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
from flask import jsonify
import datetime


res = []
p = [] # Project.select().where(True)
for x in p:
    d = model_to_dict(x)
    print type(d)
    res.append(d)
    
#print json.dumps(res)

p = Task.select()
p1 = p.where(Task.user_name == "Mia")
for x in p1:
    d = model_to_dict(x)
    print d
    
p2 = p.where(Task.date == datetime.date(2019,3,7))
for x in p2:
    d = model_to_dict(x)
    print d
