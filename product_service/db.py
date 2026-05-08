import mysql.connector
import os
import time

def get_conn():
    for i in range(10):
        try:
            return mysql.connector.connect(
                host=os.getenv("DB_HOST", "mysql"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", "root"),
                database=os.getenv("DB_NAME")
            )
        except Exception as e:
            print("Waiting for MySQL...", e)
            time.sleep(3)

    raise Exception("MySQL connection failed after retries")


def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            description TEXT,
            image_url VARCHAR(500),
            price FLOAT,
            stock INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()