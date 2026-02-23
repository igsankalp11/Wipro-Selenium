import requests

URL = "http://127.0.0.1:5000/v1/doctors"

headers = {
    "Authorization": "Bearer testtoken123",
    "Content-Type": "application/json"
}

payload = {
    "name": "Dr. Mehta",
    "specialization": "Cardiologist",
    "experience": 12
}

response = requests.post(URL, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)
