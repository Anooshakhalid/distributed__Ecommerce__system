from flask import Flask,request,jsonify
from db import get_conn,init_db
import requests

app=Flask(__name__)

init_db()

ORDER_SERVICE="http://order_service:5003"

@app.route("/pay",methods=["POST"])
def pay():

    data=request.json

    order_id=data["order_id"]

    amount=data["amount"]

    conn=get_conn()

    cur=conn.cursor()

    cur.execute("""
    INSERT INTO payments
    (amount,status)
    VALUES(%s,%s)
    """,
    (amount,"SUCCESS"))

    conn.commit()

    conn.close()


    requests.put(
        f"{ORDER_SERVICE}/confirm/{order_id}"
    )

    return jsonify({
        "status":"SUCCESS"
    })


if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=5004
    )