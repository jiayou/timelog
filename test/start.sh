#!/bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

docker run -d --name timelog-mysql -v $SCRIPTPATH/db:/db -e MYSQL_ALLOW_EMPTY_PASSWORD=1 mysql:5.7
docker run -d --name timelog-myadmin --link timelog-mysql:db -p 8306:80 phpmyadmin/phpmyadmin
sleep 1
docker ps -a

echo "waiting for mysql server start..."
sleep 5
docker exec -it timelog-mysql bash -c "service mysql status"

echo "setup databaase..."
sleep 5
docker exec -it timelog-mysql bash -c "mysql -u root < /db/setup.sql"

echo "create table user..."
sleep 5
docker exec -it timelog-mysql bash -c "mysql -u timelog < /db/user.sql"

echo "create table project..."
sleep 5
docker exec -it timelog-mysql bash -c "mysql -u timelog < /db/project.sql"

echo "create table task..."
sleep 5
docker exec -it timelog-mysql bash -c "mysql -u timelog < /db/task.sql"

echo "done."
