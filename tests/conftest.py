import pytest
from app import create_app
from flask import Flask

@pytest.fixture
def app():
    """Create and configure a test Flask application instance"""
    app = create_app('testing')
    app.config.update({
        'TESTING': True,
        'WTF_CSRF_ENABLED': False,
        'WEATHER_API_KEY': 'test_api_key',
        'WEATHER_API_URL': 'http://api.weatherapi.com/v1/current.json',
        'SECRET_KEY': 'test_secret_key'
    })
    
    yield app

@pytest.fixture
def client(app):
    """Create a test client for the app"""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create a test CLI runner for the app"""
    return app.test_cli_runner()