import os
import mysql.connector
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
    CREATE TABLE IF NOT EXISTS orders(
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        product_id INT,
        amount FLOAT,
        status VARCHAR(50) DEFAULT 'PENDING'
    )
    """)

    conn.commit()
    conn.close()