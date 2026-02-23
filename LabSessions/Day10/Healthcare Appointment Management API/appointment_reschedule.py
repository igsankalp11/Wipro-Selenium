import requests

BASE = "http://127.0.0.1:5000/v1/appointments/1"   # change id if needed

headers = {
    "Authorization": "Bearer testtoken123"
}

response = requests.get(BASE, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)
