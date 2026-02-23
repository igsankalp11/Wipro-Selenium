import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/v1"

headers = {
    "Authorization": "Bearer testtoken123",
    "Content-Type": "application/json"
}

@pytest.fixture(scope="session")
def store():
    return {}

# 1️⃣ CREATE DOCTOR
def test_create_doctor(store):
    payload = {
        "name": "Dr. Mehta",
        "specialization": "Cardiologist",
        "experience": 12
    }

    r = requests.post(f"{BASE_URL}/doctors", json=payload, headers=headers)

    assert r.status_code == 201
    store["doctor_id"] = r.json()["doctor_id"]


# 2️⃣ REGISTER PATIENT
def test_register_patient(store):
    payload = {
        "name": "Deepak",
        "age": 25,
        "phone": "9999999999",
        "email": "deepak@test.com"
    }

    r = requests.post(f"{BASE_URL}/patients", json=payload, headers=headers)

    assert r.status_code == 201
    store["patient_id"] = r.json()["patient_id"]


# EDGE CASES
def test_invalid_age():
    payload = {"name":"Bad","age":-1,"phone":"8888888888","email":"bad@test.com"}
    r = requests.post(f"{BASE_URL}/patients", json=payload, headers=headers)
    assert r.status_code == 400


def test_duplicate_phone(store):
    payload = {"name":"Dup","age":22,"phone":"9999999999","email":"dup@test.com"}
    r = requests.post(f"{BASE_URL}/patients", json=payload, headers=headers)
    assert r.status_code == 409


# 3️⃣ BOOK APPOINTMENT
def test_book_appointment(store):
    payload = {
        "patient_id": store["patient_id"],
        "doctor_id": store["doctor_id"],
        "date": "2026-03-10",
        "time": "10:00"
    }

    r = requests.post(f"{BASE_URL}/appointments", json=payload, headers=headers)

    assert r.status_code == 201
    store["appointment_id"] = r.json()["appointment_id"]


# 4️⃣ VIEW
def test_view_appointment(store):
    r = requests.get(f"{BASE_URL}/appointments/{store['appointment_id']}", headers=headers)
    assert r.status_code == 200


# 5️⃣ RESCHEDULE
def test_reschedule(store):
    payload = {"date":"2026-03-10","time":"11:00"}

    r = requests.put(f"{BASE_URL}/appointments/{store['appointment_id']}", json=payload, headers=headers)

    assert r.status_code == 200


# CONFLICT
def test_reschedule_conflict(store):
    payload = {"date":"2026-03-10","time":"11:00"}

    r = requests.put(f"{BASE_URL}/appointments/{store['appointment_id']}", json=payload, headers=headers)

    assert r.status_code == 409


# 6️⃣ CANCEL
def test_cancel(store):
    r = requests.delete(f"{BASE_URL}/appointments/{store['appointment_id']}", headers=headers)
    assert r.status_code == 204


def test_cancel_again(store):
    r = requests.delete(f"{BASE_URL}/appointments/{store['appointment_id']}", headers=headers)
    assert r.status_code in [404, 410]
