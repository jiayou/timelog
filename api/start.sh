#!/bin/bash

SCRIPTPATH=$( cd $(dirname $0); pwd)
if [[ -n $1 && $1 == 'dev' ]]
then
    NAME=timelog-api-dev
    python $SCRIPTPATH/service/app.py
else
    NAME=timelog-api
    PORT=5000
    docker run -d \
            --name $NAME \
            -p $PORT:5000 \
            -v $SCRIPTPATH/service:/service \
            -v $SCRIPTPATH/supervisor.conf:/etc/supervisor/conf.d/timelog.conf \
            timelog:python
fi

