#!/bin/bash

docker run -d --name timelog-mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=1 mysql:5.7
docker run -d --name timelog-myadmin --link timelog-mysql:db -p 8306:80 phpmyadmin/phpmyadmin
sleep 1
docker ps -a
