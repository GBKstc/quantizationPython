import mysql.connector
from flask import current_app
from mysql.connector import Error

def get_db_connection():
    return mysql.connector.connect(
        host=current_app.config['DB_HOST'],
        port=current_app.config['DB_PORT'],
        user=current_app.config['DB_USER'],
        passwd=current_app.config['DB_PASSWORD'],
        database=current_app.config['DB_NAME'],
        connect_timeout=current_app.config['DB_TIMEOUT']
    )

def fetch_data(query):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        column_names = [column[0] for column in cursor.description]
        data = [dict(zip(column_names, row)) for row in rows]
        return data, None
    except Error as e:
        return None, str(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()