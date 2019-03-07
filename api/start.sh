#!/bin/bash

SCRIPTPATH=$( cd $(dirname $0); pwd)
if [[ -n $1 && $1 == 'test' ]]
then
    NAME=timelog-api-test
    PORT=5001
else
    NAME=timelog-api
    PORT=5000
fi

docker run -d \
        --name $NAME \
        -p $PORT:5000 \
        -v $SCRIPTPATH/service:/service \
        -v $SCRIPTPATH/supervisor.conf:/etc/supervisor/conf.d/timelog.conf \
        timelog:python
