from http_methods import APIClient
from utils import assert_status_code, assert_response_body
from schemas import weather_schema
from config import Config

def test_get_weather():
    response = APIClient.get('weather',{'lat': 44.3, 'lon': 10.99, 'appid': Config.API_SECRET_KEY})
    assert_status_code(response, 200)
    assert_response_body(response, weather_schema)
