from flask import Flask, request, jsonify

app = Flask(__name__)

customers = {}
next_id = 1


# ---------- POST : CREATE ----------
@app.route("/customers", methods=["POST"])
def create_customer():
    global next_id

    data = request.json

    customer = {
        "id": next_id,
        "name": data["name"],
        "email": data["email"],
        "balance": data["balance"]
    }

    customers[next_id] = customer
    next_id += 1

    return jsonify(customer), 201


# ---------- GET : ALL CUSTOMERS ----------
@app.route("/customers", methods=["GET"])
def get_all_customers():
    return jsonify(list(customers.values())), 200


# ---------- GET : SINGLE CUSTOMER ----------
@app.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):

    if customer_id not in customers:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify(customers[customer_id]), 200


# ---------- PUT : UPDATE ----------
@app.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):

    if customer_id not in customers:
        return jsonify({"error": "Customer not found"}), 404

    data = request.json

    customers[customer_id]["name"] = data.get("name", customers[customer_id]["name"])
    customers[customer_id]["email"] = data.get("email", customers[customer_id]["email"])
    customers[customer_id]["balance"] = data.get("balance", customers[customer_id]["balance"])

    return jsonify(customers[customer_id]), 200


# ---------- DELETE ----------
@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):

    if customer_id not in customers:
        return jsonify({"error": "Customer not found"}), 404

    del customers[customer_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
