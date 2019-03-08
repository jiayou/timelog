#sh

supervisord -n  &

sleep 5
service mysqld status
mysql -u root < prepare-database.sql

while [ 1 ]; do
        echo "container running..."
        sleep 60
        test $? -gt 128 && break;
done
