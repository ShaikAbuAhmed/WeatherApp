import pytest
from app import create_app
from app.services.weather_service import WeatherService

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    app = create_app('development')
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()

def test_index_page(client):
    """Test that the index page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Weather Dashboard' in response.data

def test_weather_form_submission(client):
    """Test weather form submission with valid city."""
    response = client.post('/weather', data={'city': 'London'})
    assert response.status_code == 302  # Redirect after successful submission

def test_weather_service():
    """Test weather service with mock data."""
    # This is a basic test to ensure the service is properly configured
    assert WeatherService is not None 