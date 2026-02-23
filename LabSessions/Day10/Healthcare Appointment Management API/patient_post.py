import requests

URL = "http://127.0.0.1:5000/v1/patients"

headers = {
    "Authorization": "Bearer testtoken123",
    "Content-Type": "application/json"
}

payload = {
    "name": "Deepak",
    "age": 25,
    "phone": "9999999999",
    "email": "deepak@test.com"
}

response = requests.post(URL, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)
