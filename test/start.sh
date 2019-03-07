#!/bin/bash

docker run --name timelog-mysql -e MYSQL_ALLOW_EMPTY_PASSWORD -d mysql
docker run --name timelog-myadmin -d --link timelog-mysql:db -p 8306:80 phpmyadmin/phpmyadmin
