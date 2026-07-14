"""
Database Connection Module

This module provides database connectivity for the surveillance
system using SQLite.

Purpose:
    - Define the database location.
    - Create database connections.
    - Provide a reusable connection function for other modules.

SQLite is used because it is:
    - Lightweight
    - Serverless
    - Easy to deploy
    - Suitable for local surveillance systems

Pipeline Position:

AI Processing
       |
       ↓
Incident Data
       |
       ↓
Database Layer
       |
       ↓
SQLite Storage
"""


import sqlite3


# Database file location
DB_NAME = "community.db"



def connect():
    """
    Create and return a connection to the SQLite database.

    Returns:
        sqlite3.Connection:
            Active database connection object.

    Example:

        conn = connect()

        cursor = conn.cursor()

    """

    return sqlite3.connect(
        DB_NAME
    )