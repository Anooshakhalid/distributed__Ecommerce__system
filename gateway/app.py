from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__, template_folder="templates")

# ---------------- SERVICES ----------------
USER_SERVICE = "http://user_service:5001"
PRODUCT_SERVICE = "http://product_service:5002"
ORDER_SERVICE = "http://order_service:5003"
PAYMENT_SERVICE = "http://payment_service:5004"


# =====================================================
# UI ROUTES (FRONTEND PAGES)
# =====================================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/products")
def products_page():
    return render_template("products.html")


@app.route("/orders")
def orders_page():
    return render_template("orders.html")


@app.route("/payment/<int:order_id>")
def payment_page(order_id):
    return render_template("payment.html", order_id=order_id)


# =====================================================
# API ROUTES (GATEWAY)
# =====================================================

@app.route("/api/products", methods=["GET"])
def products():
    try:
        response = requests.get(f"{PRODUCT_SERVICE}/products")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/orders", methods=["GET", "POST"])
def orders():
    try:
        if request.method == "GET":
            response = requests.get(f"{ORDER_SERVICE}/orders")
            return jsonify(response.json())

        response = requests.post(
            f"{ORDER_SERVICE}/order",
            json=request.json
        )
        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/payment", methods=["POST"])
def payment():
    try:
        response = requests.post(
            f"{PAYMENT_SERVICE}/payment",
            json=request.json
        )
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/user/<int:user_id>")
def user(user_id):
    try:
        response = requests.get(f"{USER_SERVICE}/user/{user_id}")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =====================================================
# HEALTH CHECK
# =====================================================

@app.route("/health")
def health():
    return jsonify({
        "status": "Gateway running",
        "services": [
            USER_SERVICE,
            PRODUCT_SERVICE,
            ORDER_SERVICE,
            PAYMENT_SERVICE
        ]
    })


# =====================================================
# RUN (UI ON 5005)
# =====================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True, use_reloader=False)