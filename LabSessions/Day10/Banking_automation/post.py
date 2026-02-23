import requests

BASE_URL = "http://127.0.0.1:5000/customers"

def create_customer(payload):
    return requests.post(BASE_URL, json=payload)


if __name__ == "__main__":

    customers = [
        {"name": "Deepak Kumar", "email": "deepak@test.com", "balance": 5000},
        {"name": "Rahul Sharma", "email": "rahul@bank.com", "balance": 12000},
        {"name": "Anita Verma", "email": "anita@bank.com", "balance": 8000},
        {"name": "Priya Singh", "email": "priya@bank.com", "balance": 15000}
    ]

    for c in customers:
        r = create_customer(c)
        print(r.status_code, r.json())
