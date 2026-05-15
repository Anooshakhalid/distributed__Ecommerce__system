from flask import Flask, request, jsonify
from db import get_conn, init_db
import bcrypt

app = Flask(__name__)
init_db()


# ---------------- REGISTER ----------------
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    try:
        hashed_password = bcrypt.hashpw(
            data["password"].encode("utf-8"),
            bcrypt.gensalt()
        )

        conn = get_conn()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (data["name"], data["email"], hashed_password.decode("utf-8"))
        )

        conn.commit()
        return jsonify({"message": "User registered"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    finally:
        conn.close()


# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM users WHERE email=%s", (data["email"],))
    user = cur.fetchone()
    conn.close()

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    if not bcrypt.checkpw(
        data["password"].encode("utf-8"),
        user["password"].encode("utf-8")
    ):
        return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        }
    })


# ---------------- USERS ----------------
@app.route("/users")
def get_users():
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT id, name, email FROM users")
    users = cur.fetchall()

    conn.close()
    return jsonify(users)


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT id, name, email FROM users WHERE id=%s", (user_id,))
    user = cur.fetchone()

    conn.close()

    if user:
        return jsonify(user)

    return jsonify({"message": "User not found"}), 404


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET name=%s, email=%s WHERE id=%s",
        (data["name"], data["email"], user_id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "User updated"})


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()

    conn.close()

    return jsonify({"message": "User deleted"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)