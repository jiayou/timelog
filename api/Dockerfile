# docker build -t timelog:python .

FROM python:2.7

RUN apt update && apt install -y supervisor
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --user flask flask-cors flask-login flask-wtf peewee

EXPOSE 5000
CMD ["supervisord", "-n"]
