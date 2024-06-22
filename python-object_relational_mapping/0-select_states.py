#!/usr/bin/python3
"""
A script to list all states from the database hbtn_0e_0_usa.

This script connects to a MySQL database using provided credentials and 
retrieves all states from the 'states' table, displaying them in ascending 
order by their 'id'.

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The MySQL username to connect with.
    mysql_password: The MySQL password to connect with.
    database_name:  The name of the MySQL database to use.

Requirements:
    - The MySQL server must be running on localhost at port 3306.
    - The MySQLdb module must be installed.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Get MySQL credentials and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select all states ordered by id
    try:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
    except MySQLdb.Error as e:
        print(f"Error executing query: {e.args[0]}: {e.args[1]}")
        cursor.close()
        db.close()
        sys.exit(1)

    # Fetch all the rows from the executed query
    rows = cursor.fetchall()

    # Print the rows in the specified format
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
