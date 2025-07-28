import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="your_db_host"
    )
    return conn

def query_db(query, params=None, one=False):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query, params)
    if one:
        result = cursor.fetchone()
    else:
        result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def insert_db(query, params):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return result

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(open("schema.sql", "r").read())
    conn.commit()
    cursor.close()
    conn.close()