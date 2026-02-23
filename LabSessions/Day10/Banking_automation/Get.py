import requests

url = "http://127.0.0.1:5000/customers"

try:
    res = requests.get(url)

    if res.status_code == 200:
        print("Success")
        print(res.json())
    else:
        print("Error:", res.status_code)
        print(res.text)

except Exception as e:
    print("Request Failed:", e)
