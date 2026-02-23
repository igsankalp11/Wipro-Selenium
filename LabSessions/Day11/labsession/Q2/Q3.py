import requests
from jsonschema import validate

BASE_URL = "http://127.0.0.1:5000"


def test_profile_schema(auth_token):

    headers = {"Authorization": f"Bearer {auth_token}"}

    res = requests.get(f"{BASE_URL}/profile", headers=headers)
    assert res.status_code == 200

    response_json = res.json()

    profile_schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "role": {"type": "string"}
        },
        "required": ["name", "role"]
    }

    validate(instance=response_json, schema=profile_schema)
