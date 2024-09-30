from flask import Flask
import os
import psycopg2

app = Flask(__name__)
app.config['DEBUG'] = True

# Example route
@app.route('/')
def home():
    return "Hello from Flask with Docker Compose!"

# Connecting to the PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn

if __name__ == '__main__':
    app.run(host='0.0.0.0')
