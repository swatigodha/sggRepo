import pytest
import requests

#base url
BASE_URL = "https://restful-booker.herokuapp.com"

def test_get_booking():
    endpoint = f"{BASE_URL}/booking"
    response = requests.get(endpoint)

    assert response.status_code == 200
    print(f"Status Code: {response.status_code}")

    print(f"Response Body: {response.text}")

    print(f"Response Headers: {response.headers}")

    json_response = response.json()
    print(f"JSON Response Body: {json_response}")