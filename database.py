import os
import psycopg
from dotenv import load_dotenv

# this reads .env
load_dotenv()

def get_connection():
    # os.environ["DATABASE_URL"] retrieves that setting
    database_url = os.environ["DATABASE_URL"]
    # opens a connection from Python to Postgres
    return psycopg.connect(database_url)
