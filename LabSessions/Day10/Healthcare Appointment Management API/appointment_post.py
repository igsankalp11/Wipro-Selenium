import requests

URL = "http://127.0.0.1:5000/v1/appointments"

headers = {
    "Authorization": "Bearer testtoken123",
    "Content-Type": "application/json"
}

# change ids according to created records
payload = {
    "patient_id": 1,
    "doctor_id": 1,
    "date": "2026-03-10",
    "time": "10:00"
}

response = requests.post(URL, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)
