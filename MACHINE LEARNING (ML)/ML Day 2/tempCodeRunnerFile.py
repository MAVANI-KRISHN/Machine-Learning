
import mysql.connector
from mysql.connector import Error
import pandas as pd

# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'CarSalesDB',
    'port': 3307
}

try:
    # Establish the connection
    connection = mysql.connector.connect(**db_config)
    
    if connection.is_connected():
        print("Connected to MySQL database")

        # Define the SQL query
        query = "SELECT * FROM cars"

        # Read data into a pandas DataFrame
        df = pd.read_sql(query, connection)

        # Display the DataFrame
        # print(df.head())
        print(df)

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
