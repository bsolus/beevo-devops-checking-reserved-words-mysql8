
import mysql.connector

def check_reserved_words(database, host, user, password):
    # Connect to the database
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    
    # List of reserved words
    reserved_words = [
        "ADD", "ALTER", "AND", "ASC", "BETWEEN", "CALL", "CASCADE",
        "CASE", "CHANGE", "COLUMN", "CONSTRAINT", "CREATE", "CROSS",
        "DELETE", "DESC", "DROP", "ELSE", "EXISTS", "FALSE", "FOR",
        "FROM", "GROUP", "HAVING", "IN", "INDEX", "INSERT", "INNER",
        "JOIN", "KEY", "LEFT", "LIKE", "LIMIT", "LOAD", "LOCK", "MODIFY",
        "NOT", "NULL", "ON", "OR", "ORDER", "OUTER", "PRIMARY", "RENAME",
        "SELECT", "SET", "TABLE", "TRUE", "UPDATE", "VALUES", "WHERE", "ROW"
    ]

    # Loop through each reserved word
    for word in reserved_words:
        # Get all the tables in the database
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for table in tables:
            table_name = table[0]
            # Check if the reserved word is used as a column name in the table
            cursor.execute(f"SHOW COLUMNS FROM {table_name} LIKE '{word}'")
            result = cursor.fetchone()
            if result:
                print(f"Error: Word: '{word}' in table: `{table_name}` is a reserved word and cannot be used as a column name in MySQL 8")

check_reserved_words(database="", host="localhost", user="", password="")
