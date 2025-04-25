import os
from dotenv import load_dotenv
from pathlib import Path

# Get the absolute path to the .env file
env_path = Path(__file__).parent / '.env'

# Load environment variables from .env file
load_dotenv(dotenv_path=env_path, override=True)

class BaseConfig:
    """Base configuration class with shared settings."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
    if not WEATHER_API_KEY:
        raise ValueError("WEATHER_API_KEY environment variable is not set. Please check your .env file.")
    WEATHER_API_URL = 'http://api.weatherapi.com/v1/current.json'

class DevelopmentConfig(BaseConfig):
    """Development configuration with debug mode enabled."""
    DEBUG = True
    TESTING = False

class ProductionConfig(BaseConfig):
    """Production configuration with proper error handling."""
    DEBUG = False
    TESTING = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}