import requests

BASE_URL = "http://127.0.0.1:5000/customers"

def delete_customer(customer_id):
    return requests.delete(f"{BASE_URL}/{customer_id}")


if __name__ == "__main__":
    r = delete_customer(1)
    print(r.status_code, r.text)
