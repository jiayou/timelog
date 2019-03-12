from peewee import *

database = MySQLDatabase('timelog', **{'host': '172.17.0.2', 'charset': 'utf8', 'user': 'timelog', 'use_unicode': True})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Project(BaseModel):
    category = CharField(null=True)
    description = TextField(null=True)
    id = IntegerField(null=True)
    priority = CharField(null=True)
    project_name = CharField(null=True)

    class Meta:
        table_name = 'project'
        primary_key = False

class Task(BaseModel):
    date = DateField(null=True)
    desc = TextField(null=True)
    hours = IntegerField(null=True)
    id = IntegerField(null=True)
    project_name = CharField(null=True)
    user_name = CharField(null=True)

    class Meta:
        table_name = 'task'
        primary_key = False

class User(BaseModel):
    email = CharField(null=True)
    id = IntegerField(null=True)
    name = CharField(null=True)
    password = CharField(null=True)
    role = CharField(null=True)
    username = CharField(null=True)

    class Meta:
        table_name = 'user'
        primary_key = False

