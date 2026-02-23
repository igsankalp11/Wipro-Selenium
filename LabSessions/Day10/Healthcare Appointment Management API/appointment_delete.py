import requests

BASE = "http://127.0.0.1:5000"
TOKEN = {"Authorization": "Bearer testtoken123"}

def cancel(aid):
    return requests.delete(f"{BASE}/v1/appointments/{aid}", headers=TOKEN)
