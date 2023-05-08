import pandas as pd
import mysql.connector

# MySQL database connection parameters
host = 'localhost'
user = 'root'
password = 'password'
database = 'mydatabase'

# Connect to MySQL database
cnx = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = cnx.cursor()

# Read CSV file into a Pandas DataFrame
df = pd.read_csv('data.csv')

# Perform data transformation using Pandas
df['new_column'] = df['old_column'] * 2

# Insert transformed data into MySQL database
for index, row in df.iterrows():
    sql = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    val = (row['column1'], row['column2'])
    cursor.execute(sql, val)
    cnx.commit()

# Close database connection
cursor.close()
cnx.close()
