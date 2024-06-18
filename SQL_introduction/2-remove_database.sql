#!/bin/bash

# MySQL credentials
USER="your_mysql_username"
PASSWORD="your_mysql_password"
HOST="localhost"

# Database to be dropped
DATABASE="hbtn_0c_0"

# Command to drop the database if it exists
mysql -u"$USER" -p"$PASSWORD" -h"$HOST" -e "DROP DATABASE IF EXISTS $DATABASE;"
