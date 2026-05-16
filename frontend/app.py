from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/orders")
def orders():
    return render_template("orders.html")

@app.route("/payment/<int:order_id>")
def payment(order_id):
    return render_template("payment.html", order_id=order_id)
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


@app.route("/success")
def success():
    return render_template("success.html")
# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)