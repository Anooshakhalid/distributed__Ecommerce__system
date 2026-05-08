import mysql.connector

def get_conn():
    return mysql.connector.connect(
        host="host.docker.internal",
        user="root",
        password="",
        database="user_db"
    )

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            password VARCHAR(100)
        )
    """)

    conn.commit()
    conn.close()