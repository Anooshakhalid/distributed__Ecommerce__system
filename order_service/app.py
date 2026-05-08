from flask import Flask, request, jsonify
import requests
from db import get_conn, init_db

app = Flask(__name__)
init_db()

USER_SERVICE = "http://localhost:5001"
PRODUCT_SERVICE = "http://localhost:5002"
PAYMENT_SERVICE = "http://localhost:5004"


@app.route("/order", methods=["POST"])
def create_order():
    data = request.json

    # Get product
    product = requests.get(f"{PRODUCT_SERVICE}/product/{data['product_id']}").json()

    if "error" in product:
        return jsonify({"error": "Product not found"}), 404

    amount = product["price"]

    # Payment call
    payment = requests.post(f"{PAYMENT_SERVICE}/pay", json={"amount": amount}).json()

    status = "CONFIRMED" if payment["status"] == "SUCCESS" else "FAILED"

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO orders (user_id, product_id, amount, status)
        VALUES (%s, %s, %s, %s)
    """, (data["user_id"], data["product_id"], amount, status))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Order processed",
        "status": status,
        "amount": amount
    })


@app.route("/orders", methods=["GET"])
def get_orders():
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM orders")
    data = cur.fetchall()

    conn.close()
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)