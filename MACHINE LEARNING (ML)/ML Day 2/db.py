import pandas as pd
import mysql.connector
from mysql.connector import Error

# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': '',  
    'database': 'CarSalesDB',     
    'port': 3307                   
}

# Path to the CSV file
csv_file_path = r'C:\Users\HP\OneDrive\Desktop\BIA\Machine Learning\Day 2 Homework\car data.csv'

def import_csv_to_mysql():
    connection = None
    try:
        # Establish the database connection
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database")

            # Create a cursor object
            cursor = connection.cursor()

            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(csv_file_path)

            # Iterate over DataFrame rows and insert into the table
            insert_query = """
                INSERT INTO cars (Car_Name, Year, Selling_Price, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            data_tuples = [
                (
                    row['Car_Name'],
                    int(row['Year']),
                    float(row['Selling_Price']),
                    float(row['Present_Price']),
                    int(row['Kms_Driven']),
                    row['Fuel_Type'],
                    row['Seller_Type'],
                    row['Transmission'],
                    int(row['Owner'])
                )
                for index, row in df.iterrows()
            ]

            cursor.executemany(insert_query, data_tuples)

            # Commit the transaction
            connection.commit()
            print(f"{cursor.rowcount} records inserted successfully into 'cars' table.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    import_csv_to_mysql()


