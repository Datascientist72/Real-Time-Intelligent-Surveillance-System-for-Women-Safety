import sqlite3

DB_NAME = "community.db"

def connect():

    return sqlite3.connect(DB_NAME)