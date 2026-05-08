from flask import Flask, request, jsonify
from db import get_conn, init_db

app = Flask(__name__)
init_db()

@app.route("/register", methods=["POST"])
def register():
    data = request.json

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (data["name"], data["email"], data["password"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "User registered"})


@app.route("/login", methods=["POST"])
def login():
    data = request.json

    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM users WHERE email=%s AND password=%s",
                (data["email"], data["password"]))

    user = cur.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "Login successful", "user": user})
    return jsonify({"message": "Invalid credentials"}), 401


@app.route("/users", methods=["GET"])
def users():
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM users")
    data = cur.fetchall()

    conn.close()
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)