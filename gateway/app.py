from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------------- SERVICES ----------------
USER_SERVICE = "http://localhost:5001"
PRODUCT_SERVICE = "http://localhost:5002"
ORDER_SERVICE = "http://localhost:5003"
PAYMENT_SERVICE = "http://localhost:5004"


# ---------------- PRODUCTS ----------------

@app.route("/api/products", methods=["GET"])
def products():
    try:
        res = requests.get(
            f"{PRODUCT_SERVICE}/products"
        )

        return jsonify(
            res.json()
        )

    except Exception as e:

        return jsonify({
            "error": str(e)
        }),500


# ---------------- ORDERS ----------------

@app.route(
"/api/orders",
methods=["GET","POST"]
)
def orders():

    try:

        if request.method=="GET":

            res=requests.get(
                f"{ORDER_SERVICE}/orders"
            )

            return jsonify(
                res.json()
            )


        res=requests.post(
            f"{ORDER_SERVICE}/order",
            json=request.json
        )

        return jsonify(
            res.json()
        )

    except Exception as e:

        return jsonify({
            "error":str(e)
        }),500



# ================= NEW CHECKOUT =================



@app.route("/api/checkout", methods=["POST"])
def checkout():

    try:

        res = requests.post(
            f"{ORDER_SERVICE}/checkout",
            json=request.json
        )

        print("STATUS:", res.status_code)
        print("TEXT:", res.text)

        return jsonify(
            res.json()
        ), res.status_code

    except Exception as e:

        return jsonify({
            "error": str(e)
        }),500
# ================= NEW PAY =================

@app.route(
"/api/pay",
methods=["POST"]
)

def pay():

    try:

        res=requests.post(

            f"{PAYMENT_SERVICE}/pay",

            json=request.json

        )

        return jsonify(
            res.json()
        )

    except Exception as e:

        return jsonify({
            "error":str(e)
        }),500



# ---------------- USER ----------------

@app.route("/api/user", methods=["GET"])
def get_users():

    res=requests.get(
        f"{USER_SERVICE}/users"
    )

    data=res.json()

    if isinstance(data,list):

        for u in data:
            u.pop("password",None)

    else:

        data.pop(
            "password",
            None
        )

    return jsonify(data)



@app.route(
"/api/user/login",
methods=["POST"]
)
def login_user():

    try:

        res=requests.post(

            f"{USER_SERVICE}/login",

            json=request.json

        )

        return jsonify(
            res.json()
        ),res.status_code


    except Exception as e:

        return jsonify({
            "error":str(e)
        }),500




@app.route(
"/api/user/register",
methods=["POST"]
)
def register_user():

    try:

        res=requests.post(

            f"{USER_SERVICE}/register",

            json=request.json

        )

        return jsonify(
            res.json()
        ),res.status_code


    except Exception as e:

        return jsonify({
            "error":str(e)
        }),500



# ---------------- RUN ----------------

if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )