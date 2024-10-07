import pytest
from jsonschema import validate

def assert_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code, \
        f"Expected status code to be {expected_status_code}, but got {response.status_code}"

def assert_response_body(response, expected_body):
    assert response.json() == expected_body, \
        f"Expected response body to be {expected_body}, but got {response.json()}"