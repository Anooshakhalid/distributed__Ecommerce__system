from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Phone", "price": 800}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/product/<int:pid>', methods=['GET'])
def get_product(pid):
    for p in products:
        if p['id'] == pid:
            return jsonify(p)
    return jsonify({"error": "Not found"}), 404

@app.route('/add', methods=['POST'])
def add_product():
    data = request.json
    products.append(data)
    return jsonify({"message": "Product added"})

if __name__ == '__main__':
    app.run(port=5002)