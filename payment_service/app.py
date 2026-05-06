from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/pay', methods=['POST'])
def pay():
    data = request.json
    amount = data['amount']

    # Simulated payment success/failure
    if random.choice([True, True, False]):  # mostly success
        return jsonify({"status": "SUCCESS", "amount": amount})
    else:
        return jsonify({"status": "FAILED", "amount": amount})

if __name__ == '__main__':
    app.run(port=5004)