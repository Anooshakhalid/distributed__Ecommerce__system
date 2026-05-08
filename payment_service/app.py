from flask import Flask, request, jsonify
import random
from db import get_conn, init_db

app = Flask(__name__)
init_db()

@app.route("/pay", methods=["POST"])
def pay():
    data = request.json
    amount = data["amount"]

    status = "SUCCESS" if random.random() > 0.3 else "FAILED"

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO payments (amount, status) VALUES (%s, %s)",
        (amount, status)
    )

    conn.commit()
    conn.close()

    return jsonify({"status": status, "amount": amount})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)