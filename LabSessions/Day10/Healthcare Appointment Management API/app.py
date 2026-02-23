from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = "testtoken123"

doctors = {}
patients = {}
appointments = {}

doctor_id = 1
patient_id = 1
appointment_id = 1


# ---------- AUTH ----------
def authorized(req):
    return req.headers.get("Authorization") == f"Bearer {TOKEN}"


# ---------- CREATE DOCTOR ----------
@app.route("/v1/doctors", methods=["POST"])
def create_doctor():
    global doctor_id

    if not authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json

    doc = {
        "doctor_id": doctor_id,
        "name": data["name"],
        "specialization": data["specialization"],
        "experience": data["experience"]
    }

    doctors[doctor_id] = doc
    doctor_id += 1

    return jsonify(doc), 201

# ---------- GET ALL DOCTORS ----------
@app.route("/v1/doctors", methods=["GET"])
def get_all_doctors():
    if not authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify(list(doctors.values())), 200


# ---------- GET SINGLE DOCTOR ----------
@app.route("/v1/doctors/<int:did>", methods=["GET"])
def get_doctor(did):

    if not authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    if did not in doctors:
        return jsonify({"error": "Doctor not found"}), 404

    return jsonify(doctors[did]), 200

# ---------- REGISTER PATIENT ----------
@app.route("/v1/patients", methods=["POST"])
def register_patient():
    global patient_id

    if not authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json

    if data.get("age", 0) < 0:
        return jsonify({"error": "Invalid age"}), 400

    if "email" not in data:
        return jsonify({"error": "Missing email"}), 400

    for p in patients.values():
        if p["phone"] == data["phone"]:
            return jsonify({"error": "Duplicate phone"}), 409

    pat = {
        "patient_id": patient_id,
        "name": data["name"],
        "age": data["age"],
        "phone": data["phone"],
        "email": data["email"]
    }

    patients[patient_id] = pat
    patient_id += 1

    return jsonify(pat), 201


# ---------- BOOK APPOINTMENT ----------
@app.route("/v1/appointments", methods=["POST"])
def book_appointment():
    global appointment_id

    if not authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json

    for a in appointments.values():
        if a["doctor_id"] == data["doctor_id"] and a["date"] == data["date"] and a["time"] == data["time"]:
            return jsonify({"error": "Slot already booked"}), 409

    app_data = {
        "appointment_id": appointment_id,
        "patient_id": data["patient_id"],
        "doctor_id": data["doctor_id"],
        "date": data["date"],
        "time": data["time"]
    }

    appointments[appointment_id] = app_data
    appointment_id += 1

    return jsonify(app_data), 201


# ---------- VIEW APPOINTMENT ----------
@app.route("/v1/appointments/<int:aid>", methods=["GET"])
def view_appointment(aid):

    if not authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    if aid not in appointments:
        return jsonify({"error": "Not found"}), 404

    return jsonify(appointments[aid]), 200


# ---------- RESCHEDULE ----------
@app.route("/v1/appointments/<int:aid>", methods=["PUT"])
def reschedule(aid):

    if not authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    if aid not in appointments:
        return jsonify({"error": "Not found"}), 404

    data = request.json

    for a in appointments.values():
        if a["doctor_id"] == appointments[aid]["doctor_id"] and a["date"] == data["date"] and a["time"] == data["time"]:
            return jsonify({"error": "Slot conflict"}), 409

    appointments[aid]["date"] = data["date"]
    appointments[aid]["time"] = data["time"]

    return jsonify(appointments[aid]), 200


# ---------- CANCEL ----------
@app.route("/v1/appointments/<int:aid>", methods=["DELETE"])
def cancel(aid):

    if not authorized(request):
        return jsonify({"error": "Unauthorized"}), 401

    if aid not in appointments:
        return jsonify({"error": "Gone"}), 410

    del appointments[aid]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
