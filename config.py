import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    BASE_URL = 'https://api.openweathermap.org/data/2.5'
    API_SECRET_KEY = os.getenv('API_SECRET_KEY')
    @staticmethod
    def set_domain(domain:str, api_secret_key:str=None):
        Config.BASE_URL = domain
        Config.API_SECRET_KEY = os.getenv('API_SECRET_KEY') if api_secret_key is None else api_secret_key