import mysql.connector

def get_conn():
    return mysql.connector.connect(
        host="host.docker.internal",
        user="root",
        password="",
        database="order_db"
    )

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            product_id INT,
            amount FLOAT,
            status VARCHAR(50)
        )
    """)

    conn.commit()
    conn.close()