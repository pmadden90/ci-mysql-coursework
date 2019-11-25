import os
import pymysql

# Get username from Workspace
# (Modify this variable if running on different environment)
username = os.getenv('GITPOD_PM')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username, password='', db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    # Close connection regardless of whether the above was successful or not
    connection.close()
