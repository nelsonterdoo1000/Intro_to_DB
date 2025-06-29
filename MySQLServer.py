#!/usr/bin/env python3
"""
MySQLServer.py - Script to create alx_book_store database
This script connects to MySQL server and creates the alx_book_store database
if it doesn't already exist.
"""

import mysql.connector
from mysql.connector import Error


def create_database():
    """
    Creates the alx_book_store database in MySQL server.
    Handles connection errors and ensures proper cleanup.
    """
    connection = None
    cursor = None
    
    try:
        # MySQL connection parameters
        connection_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'your_password_here',
            'auth_plugin': 'mysql_native_password'
        }
        
        # Establish connection to MySQL server
        print("Connecting to MySQL server...")
        connection = mysql.connector.connect(**connection_config)
        
        if connection.is_connected():
            print("Successfully connected to MySQL server")
            
            # Create cursor object
            cursor = connection.cursor()
            
            # Create database query with IF NOT EXISTS to avoid errors if database exists
            create_database_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            
            # Execute the create database command
            cursor.execute(create_database_query)
            
            # Commit the transaction
            connection.commit()
            
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:
        print(f"Error: Failed to connect to MySQL server or create database")
        print(f"MySQL Error: {e}")
        
    except Exception as e:
        print(f"Error: An unexpected error occurred")
        print(f"Exception: {e}")
        
    finally:
        # Ensure proper cleanup of database resources
        if cursor:
            cursor.close()
            print("MySQL cursor closed")
            
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed")


def main():
    """
    Main function to execute the database creation process.
    """
    print("=" * 50)
    print("ALX Book Store Database Creation Script")
    print("=" * 50)
    
    create_database()
    
    print("=" * 50)
    print("Script execution completed")
    print("=" * 50)


if __name__ == "__main__":
    main()