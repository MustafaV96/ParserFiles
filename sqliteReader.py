import sqlite3
import datetime


# Connect to the database
#conn = psycopg2.connect(
#    host="hostname",
#    user="username",
#    password="password",
#    dbname="database_name"
#)

# Connect to the database file
conn = sqlite3.connect("History")

# Create a cursor object
cur = conn.cursor()

# Execute a SELECT statement
cur.execute("SELECT start_time FROM downloads")

# Fetch all rows
rows = cur.fetchall()

# Iterate through the rows
for i in range(0, len(rows)):
    #print(row[0])
    #Convert a chrome timestamp
    timestamp = datetime.datetime(1601,1,1) + datetime.timedelta(microseconds=rows[i][0])
    print(timestamp)


#dt_object = datetime.datetime(1601,1,1) + datetime.timedelta(microseconds=timestamp)

# Close the cursor and connection
cur.close()
conn.close()
