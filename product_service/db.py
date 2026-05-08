import mysql.connector

def get_conn():
    return mysql.connector.connect(
        host="host.docker.internal",
        user="root",
        password="",
        database="product_db"
    )

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