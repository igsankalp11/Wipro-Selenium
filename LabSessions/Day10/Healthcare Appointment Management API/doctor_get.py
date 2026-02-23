import requests

BASE = "http://127.0.0.1:5000/v1/doctors"

headers = {
    "Authorization": "Bearer testtoken123"
}

# get all doctors
response = requests.get(BASE, headers=headers)

print("All Doctors:")
print(response.status_code)
print(response.text)


# get single doctor (id = 1)
response = requests.get(f"{BASE}/1", headers=headers)

print("\nSingle Doctor:")
print(response.status_code)
print(response.text)
