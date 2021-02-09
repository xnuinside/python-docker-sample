import os
import logging
import urllib.parse
import psycopg2


logger = logging.getLogger(__name__)


def test_db_connection():

    db_pass = urllib.parse.quote(os.environ.get("DB_PASS", ""))
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"), 
        dbname=os.environ.get("DB_NAME"), 
        user=os.environ.get("DB_USER"), 
        password=db_pass, 
        port=os.environ.get("DB_PORT"))
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);")
    logger.info('Connected to PostgreSQL database')


test_db_connection()
