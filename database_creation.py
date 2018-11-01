#This file creates the database

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_connection("animedatabase.db")
