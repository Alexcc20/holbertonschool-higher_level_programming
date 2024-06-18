#!/bin/bash

# Script to delete the database hbtn_0c_0 in your MySQL server.
# If the database hbtn_0c_0 doesn’t exist, the script will not fail.
# You are not allowed to use the SELECT or SHOW statements.

# MySQL credentials
# Replace 'your_mysql_username' and 'your_mysql_password' with your actual MySQL username and password
USER="your_mysql_username"
PASSWORD="your_mysql_password"
HOST="localhost"

# Name of the database to be dropped
DATABASE="hbtn_0c_0"

# Command to drop the database if it exists
# The -u option specifies the MySQL username
# The -p option specifies the MySQL password
# The -h option specifies the MySQL host
# The -e option allows you to pass the SQL command to be executed
mysql -u"$USER" -p"$PASSWORD" -h"$HOST" -e "DROP DATABASE IF EXISTS $DATABASE;"
