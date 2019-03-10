from peewee import *

database = MySQLDatabase('timelog', **{'host': '172.17.0.2', 'charset': 'utf8', 'user': 'root', 'use_unicode': True})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Project(BaseModel):
    category = IntegerField(null=True)
    description = CharField(null=True)
    name = CharField(null=True)
    priority = IntegerField(null=True)

    class Meta:
        table_name = 'project'

class Task(BaseModel):
    date = DateField(null=True)
    desc = CharField(null=True)
    hours = IntegerField(null=True)
    project_id = IntegerField(null=True)
    user_name = CharField(null=True)

    class Meta:
        table_name = 'task'

class User(BaseModel):
    email = CharField(null=True)
    name = CharField(null=True)
    password = CharField(null=True)
    role = CharField(null=True)
    username = CharField(primary_key=True)

    class Meta:
        table_name = 'user'

