import mysql.connector

def create_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    cur = conn.cursor()

    # Create databases
    cur.execute("CREATE DATABASE IF NOT EXISTS user_db")
    cur.execute("CREATE DATABASE IF NOT EXISTS product_db")
    cur.execute("CREATE DATABASE IF NOT EXISTS order_db")
    cur.execute("CREATE DATABASE IF NOT EXISTS payment_db")

    print("Databases created successfully!")

    conn.close()

if __name__ == "__main__":
    create_db()