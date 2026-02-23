import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/customers"


@pytest.fixture(scope="session")
def customer():
    return {}


# ---------------- STEP 1 : POST ----------------
def test_create_customer(customer):

    payload = {
        "name": "Deepak Kumar",
        "email": "deepak@test.com",
        "balance": 5000
    }

    response = requests.post(BASE_URL, json=payload)

    # validations
    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["name"] == payload["name"]

    # store id for next tests
    customer["id"] = data["id"]
    customer["email"] = payload["email"]
    customer["balance"] = payload["balance"]


# ---------------- STEP 2 : GET ----------------
def test_get_customer(customer):

    response = requests.get(f"{BASE_URL}/{customer['id']}")

    assert response.status_code == 200

    data = response.json()
    assert data["email"] == customer["email"]
    assert data["balance"] == customer["balance"]


# ---------------- STEP 3 : PUT ----------------
def test_update_customer(customer):

    update_payload = {
        "email": "updated@test.com"
    }

    response = requests.put(f"{BASE_URL}/{customer['id']}", json=update_payload)

    assert response.status_code == 200

    data = response.json()
    assert data["email"] == "updated@test.com"
    assert data["id"] == customer["id"]

    customer["email"] = "updated@test.com"


# ---------------- STEP 4 : DELETE ----------------
def test_delete_customer(customer):

    response = requests.delete(f"{BASE_URL}/{customer['id']}")

    assert response.status_code == 204

    # verify deletion
    response = requests.get(f"{BASE_URL}/{customer['id']}")
    assert response.status_code == 404
