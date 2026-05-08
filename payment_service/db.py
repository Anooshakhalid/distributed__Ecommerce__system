import mysql.connector

def get_conn():
    return mysql.connector.connect(
        host="host.docker.internal",
        user="root",
        password="",
        database="payment_db"
    )

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            amount FLOAT,
            status VARCHAR(20)
        )
    """)

    conn.commit()
    conn.close()