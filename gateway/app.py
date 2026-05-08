# main.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

USER_SERVICE = "http://localhost:5001"
PRODUCT_SERVICE = "http://localhost:5002"
ORDER_SERVICE = "http://localhost:5003"

@app.route("/api/products")
def products():
    return requests.get(f"{PRODUCT_SERVICE}/products").json()

@app.route("/api/order", methods=["POST"])
def order():
    return requests.post(f"{ORDER_SERVICE}/order", json=request.json).json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)