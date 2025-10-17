from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'db'),
        database=os.getenv('POSTGRES_DB', 'testdb'),
        user=os.getenv('POSTGRES_USER', 'testuser'),
        password=os.getenv('POSTGRES_PASSWORD', 'testpass')
    )
    return conn

@app.route('/')
def hello():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        conn.close()
        return "Привет Докер и postgres!"
    except Exception:
        return "Извините, но подключения к базе не случилось :("

if __name__ == '__main__':
    app_port = int(os.getenv('APP_PORT', 1234))
    app.run(host='0.0.0.0', port=app_port)