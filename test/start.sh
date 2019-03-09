#!/bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

docker run -d --name timelog-mysql -v $SCRIPTPTH/db:/db -e MYSQL_ALLOW_EMPTY_PASSWORD=1 mysql:5.7
docker run -d --name timelog-myadmin --link timelog-mysql:db -p 8306:80 phpmyadmin/phpmyadmin
sleep 1
docker ps -a


docker exec -it timelog-mysql bash -c "service mysqld status"
docker exec -it timelog-mysql bash -c "mysql -u root < /db/prepare-database.sql"

