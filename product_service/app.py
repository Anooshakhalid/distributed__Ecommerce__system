from flask import Flask, request, jsonify
from db import get_conn, init_db

app = Flask(__name__)
init_db()

# ---------------------------
# CREATE PRODUCT (SINGLE + BULK)
# ---------------------------
@app.route("/products", methods=["POST"])
def add_product():
    try:
        data = request.json

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        conn = get_conn()
        cur = conn.cursor()

        # ---------------------------
        # BULK INSERT (LIST)
        # ---------------------------
        if isinstance(data, list):

            values = []

            for item in data:
                if not all(k in item for k in ("name", "price", "stock")):
                    return jsonify({"error": "Missing fields in one or more items"}), 400

                values.append((item["name"], item["price"], item["stock"]))

            cur.executemany(
                "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
                values
            )

        # ---------------------------
        # SINGLE INSERT (DICT)
        # ---------------------------
        else:
            if not all(k in data for k in ("name", "price", "stock")):
                return jsonify({"error": "Missing fields"}), 400

            cur.execute(
                "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
                (data["name"], data["price"], data["stock"])
            )

        conn.commit()
        conn.close()

        return jsonify({"message": "Product(s) added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------------
# GET ALL PRODUCTS
# ---------------------------
@app.route("/products", methods=["GET"])
def get_products():
    try:
        conn = get_conn()
        cur = conn.cursor(dictionary=True)

        cur.execute("SELECT * FROM products")
        data = cur.fetchall()

        conn.close()
        return jsonify(data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------------
# GET SINGLE PRODUCT
# ---------------------------
@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    try:
        conn = get_conn()
        cur = conn.cursor(dictionary=True)

        cur.execute("SELECT * FROM products WHERE id=%s", (id,))
        product = cur.fetchone()

        conn.close()

        if product:
            return jsonify(product), 200

        return jsonify({"error": "Product not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------------
# UPDATE PRODUCT
# ---------------------------
@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    try:
        data = request.json

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        conn = get_conn()
        cur = conn.cursor()

        cur.execute("SELECT * FROM products WHERE id=%s", (id,))
        if not cur.fetchone():
            conn.close()
            return jsonify({"error": "Product not found"}), 404

        cur.execute(
            "UPDATE products SET name=%s, price=%s, stock=%s WHERE id=%s",
            (data["name"], data["price"], data["stock"], id)
        )

        conn.commit()
        conn.close()

        return jsonify({"message": "Product updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------------
# DELETE PRODUCT
# ---------------------------
@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    try:
        conn = get_conn()
        cur = conn.cursor()

        cur.execute("SELECT * FROM products WHERE id=%s", (id,))
        if not cur.fetchone():
            conn.close()
            return jsonify({"error": "Product not found"}), 404

        cur.execute("DELETE FROM products WHERE id=%s", (id,))

        conn.commit()
        conn.close()

        return jsonify({"message": "Product deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------------
# RUN SERVER
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)