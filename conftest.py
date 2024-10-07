import pytest
from config import Config

@pytest.fixture(scope='session', autouse=True)
def set_base_url():
    Config.set_domain('https://api.openweathermap.org/data/2.5')