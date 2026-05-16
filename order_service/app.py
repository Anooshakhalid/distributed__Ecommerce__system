# from flask import Flask,request,jsonify
# import requests
# from db import get_conn,init_db

# app=Flask(__name__)
# init_db()

# PRODUCT_SERVICE="http://product_service:5002"

# @app.route("/checkout",methods=["POST"])
# def checkout():

#     data=request.json

#     product=requests.get(
#         f"{PRODUCT_SERVICE}/product/{data['product_id']}"
#     ).json()

#     if "error" in product:
#         return jsonify({"error":"Product not found"}),404


#     conn=get_conn()

#     cur=conn.cursor()

#     cur.execute("""
#     INSERT INTO orders
#     (user_id,product_id,amount,status)
#     VALUES(%s,%s,%s,%s)
#     """,
#     (
#         data["user_id"],
#         data["product_id"],
#         product["price"],
#         "PENDING"
#     ))

#     conn.commit()

#     order_id=cur.lastrowid

#     conn.close()

#     return jsonify({

#         "message":"Checkout created",
#         "order_id":order_id,
#         "amount":product["price"]

#     })


# @app.route("/confirm/<int:order_id>",methods=["PUT"])
# def confirm(order_id):

#     conn=get_conn()

#     cur=conn.cursor()

#     cur.execute("""
#     UPDATE orders
#     SET status='CONFIRMED'
#     WHERE id=%s
#     """,(order_id,))

#     conn.commit()

#     conn.close()

#     return jsonify({
#         "message":"Order confirmed"
#     })


# @app.route("/orders")
# def orders():

#     conn=get_conn()

#     cur=conn.cursor(dictionary=True)

#     cur.execute("SELECT * FROM orders")

#     data=cur.fetchall()

#     conn.close()

#     return jsonify(data)


# if __name__=="__main__":
#     app.run(
#         host="0.0.0.0",
#         port=5003
#     )
from flask import Flask,request,jsonify
import requests
from db import get_conn,init_db

app=Flask(__name__)
init_db()

PRODUCT_SERVICE="http://product_service:5002"


@app.route("/checkout",methods=["POST"])
def checkout():

    try:

        data=request.json

        res=requests.get(
            f"{PRODUCT_SERVICE}/products/{data['product_id']}"
        )

        print("PRODUCT STATUS:",res.status_code)
        print("PRODUCT DATA:",res.text)

        if res.status_code!=200:

            return jsonify({
                "error":"Product not found"
            }),404


        product=res.json()


        conn=get_conn()

        cur=conn.cursor()

        cur.execute("""

        INSERT INTO orders
        (
        user_id,
        product_id,
        amount,
        status
        )

        VALUES
        (%s,%s,%s,%s)

        """,

        (

        data["user_id"],

        data["product_id"],

        product["price"],

        "PENDING"

        ))

        conn.commit()

        order_id=cur.lastrowid

        conn.close()


        return jsonify({

            "message":"Checkout created",

            "order_id":order_id,

            "amount":product["price"]

        })

    except Exception as e:

        return jsonify({
            "error":str(e)
        }),500



@app.route(
"/confirm/<int:order_id>",
methods=["PUT"]
)
def confirm(order_id):

    conn=get_conn()

    cur=conn.cursor()

    cur.execute(
    """
    UPDATE orders
    SET status='CONFIRMED'
    WHERE id=%s
    """,
    (order_id,)
    )

    conn.commit()

    conn.close()

    return jsonify({

    "message":
    "Order confirmed"

    })


@app.route("/orders")
def orders():

    conn=get_conn()

    cur=conn.cursor(
    dictionary=True
    )

    cur.execute(
    "SELECT * FROM orders"
    )

    data=cur.fetchall()

    conn.close()

    return jsonify(data)


if __name__=="__main__":

    app.run(
    host="0.0.0.0",
    port=5003
    )