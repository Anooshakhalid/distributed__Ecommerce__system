from flask import Flask, request, jsonify
from db import get_conn, init_db

app = Flask(__name__)
init_db()

@app.route("/add", methods=["POST"])
def add_product():
    data = request.json

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
        (data["name"], data["price"], data["stock"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Product added"})


@app.route("/products", methods=["GET"])
def get_products():
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM products")
    data = cur.fetchall()

    conn.close()
    return jsonify(data)


@app.route("/product/<int:id>", methods=["GET"])
def get_product(id):
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM products WHERE id=%s", (id,))
    product = cur.fetchone()

    conn.close()

    if product:
        return jsonify(product)
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)