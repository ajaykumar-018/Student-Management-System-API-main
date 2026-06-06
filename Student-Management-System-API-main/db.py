import os
import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "Ajay@1906"),
        database=os.getenv("DB_NAME", "student_db"),
        connection_timeout=10
    )
    return connection


if __name__ == "__main__":
    connection = None
    try:
        connection = get_db_connection()
        print("Database connected successfully!")
    except Exception as e:
        print("Database connection failed:")
        print(e)
    finally:
        if connection is not None:
            connection.close()