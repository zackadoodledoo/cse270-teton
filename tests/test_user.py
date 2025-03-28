import requests
import pytest
from unittest.mock import patch

def mock_requests_get(url, params=None, **kwargs):
    if params == {"username": "admin", "password": "admin"}:
        return MockResponse("", 401)
    elif params == {"username": "admin", "password": "qwerty"}:
        return MockResponse("", 200)
    return MockResponse("Invalid request", 400)

class MockResponse:
    def __init__(self, text, status_code):
        self.text = text
        self.status_code = status_code
        self.headers = {"Content-Type": "text/plain"}

def test_unauthorized_access():
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "admin"}
    with patch("requests.get", side_effect=mock_requests_get):
        response = requests.get(url, params=params)
    
        assert response.status_code == 401, f"Expected 401, got {response.status_code}"
        assert response.text == "", f"Expected empty response, got {response.text}"

def test_authorized_access():
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "qwerty"}
    with patch("requests.get", side_effect=mock_requests_get):
        response = requests.get(url, params=params)
    
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.text == "", f"Expected empty response, got {response.text}"

if __name__ == "__main__":
    pytest.main()
