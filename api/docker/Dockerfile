# docker build -t timelog:python .

FROM daocloud.io/library/python:2.7.13-stretch
# RUN sed -i -E 's/\w+\.debian\.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y supervisor

RUN pip install flask flask-cors peewee pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 5000
CMD ["supervisord", "-n"]


# # pip freeze
# Click==7.0
# Flask==1.0.2
# Flask-Cors==3.0.7
# itsdangerous==1.1.0
# Jinja2==2.10
# MarkupSafe==1.1.1
# peewee==3.9.2
# PyMySQL==0.9.3
# six==1.12.0
# virtualenv==15.1.0
# Werkzeug==0.14.1
