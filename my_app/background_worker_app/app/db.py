import psycopg2
import os
from dotenv import load_dotenv
DATABASE_CONFIG = {
    'dbname': os.getenv('DATABASE_NAME'),
    'user': os.getenv('DATABASE_USER'),
    'password': os.getenv('DATABASE_PASSWORD'),
    'host': os.getenv('DATABASE_HOST'),
    'port': os.getenv('DATABASE_PORT')
}


def get_db_connection():
    try:
        connection = psycopg2.connect(**DATABASE_CONFIG)
        return connection
    except Exception as e:
        print(f"Database connection error: {e}")
        return None
