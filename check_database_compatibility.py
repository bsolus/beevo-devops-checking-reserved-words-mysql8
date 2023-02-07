import mysql.connector

def check_database_compatibility(database, host, user, password):
    # Connect to the database
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()

    # Select the table_schema, table_name, and column_name for each column in the database
    cursor.execute("SELECT table_schema, table_name, column_name FROM information_schema.columns")
    columns = cursor.fetchall()

    # Loop through each column
    for column in columns:
        table_schema = column[0]
        table_name = column[1]
        column_name = column[2]

        # Check if the column uses the MySQL 8 engine
        cursor.execute(f"SELECT ENGINE FROM information_schema.tables WHERE table_schema='{table_schema}' AND table_name='{table_name}'")
        result = cursor.fetchone()
        if result and result[0] != "InnoDB":
            print(f"Warning: Table '{table_schema}.{table_name}' uses the '{result[0]}' engine, which may not be fully compatible with MySQL 8")

check_database_compatibility(database="", host="localhost", user="", password="")
