from flask import Flask, request, jsonify

app = Flask(__name__)

users_data = []

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    users_data.append(data)
    return jsonify({"message": "User added", "data": data}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users_data), 200

@app.route('/users/<int:index>', methods=['PUT'])
def update_user(index):
    data = request.json
    if index < len(users_data):
        users_data[index] = data
        return jsonify({"message": "User updated", "data": data}), 200
    return jsonify({"message": "User not found"}), 404

@app.route('/users/<int:index>', methods=['DELETE'])
def delete_user(index):
    if index < len(users_data):
        deleted = users_data.pop(index)
        return jsonify({"message": "User deleted", "data": deleted}), 200
    return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
