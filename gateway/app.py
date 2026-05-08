from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

USER_SERVICE = "http://localhost:5001"
PRODUCT_SERVICE = "http://localhost:5002"
ORDER_SERVICE = "http://localhost:5003"
PAYMENT_SERVICE = "http://localhost:5004"


# HOME PAGE (VERY IMPORTANT FOR DEMO)
@app.route("/")
def home():
    return jsonify({
        "message": "Bouquet E-Commerce SERVICES",
        "services": {
            "products": "/api/products",
            "order": "/api/order"
        }
    })


# GET ALL PRODUCTS
@app.route("/api/products")
def products():
    try:
        response = requests.get(f"{PRODUCT_SERVICE}/products")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({
            "error": "Product service not reachable",
            "details": str(e)
        }), 500


# PLACE ORDER
@app.route("/api/order", methods=["POST"])
def order():
    try:
        response = requests.post(
            f"{ORDER_SERVICE}/order",
            json=request.json
        )
        return jsonify(response.json())
    except Exception as e:
        return jsonify({
            "error": "Order service not reachable",
            "details": str(e)
        }), 500


# HEALTH CHECK
@app.route("/health")
def health():
    return jsonify({"status": "Gateway is running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)