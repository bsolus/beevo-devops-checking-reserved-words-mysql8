# Checking for Reserved Words in a MySQL 8 Database

This script checks if any reserved words are being used as column names in a MySQL 8 database.

## Requirements

- Python 3
- mysql-connector-python (install using `pip install mysql-connector-python`)

## Usage

Save the script in a file with a .py extension (e.g. check_reserved_words.py)
Open the terminal or command prompt and navigate to the folder where the script is saved
Run the following command: `python check_reserved_words.py`
On Mac and Linux, you may need to use python3 instead of python, depending on your system setup.

The script will connect to the specified database, check if any of the reserved words are being used as column names, and print out any errors.

## Configuration

Before running the script, you need to configure the following variables in the script:

`database`: the name of the database you want to connect to
`host`: the host name or IP address of the database server
`user`: the username used to connect to the database
`password`: the password used to connect to the database

## Troubleshooting

If you get an error message "ImportError: 'mysql.connector' could not be resolved", it means that the `mysql-connector-python` package is not installed in your environment. To resolve this issue, run the following command: `pip install mysql-connector-python`.

## License

This script is licensed under the MIT License.

## Copyright

Copyright (c) 2023 bsolus. All rights reserved.
