import requests

BASE_URL = "http://127.0.0.1:5000/customers"

def update_customer(customer_id, payload):
    return requests.put(f"{BASE_URL}/{customer_id}", json=payload)


if __name__ == "__main__":
    payload = {"email": "updated@test.com"}
    r = update_customer(1, payload)
    print(r.status_code, r.text)
