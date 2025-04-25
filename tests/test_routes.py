import pytest
import responses
from flask import url_for

@pytest.fixture
def mock_weather_data():
    return {
        "location": {
            "name": "London",
            "country": "United Kingdom"
        },
        "current": {
            "temp_c": 15,
            "condition": {
                "text": "Partly cloudy",
                "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png"
            },
            "humidity": 71,
            "wind_kph": 15.1,
            "wind_dir": "WSW",
            "pressure_mb": 1015.0,
            "vis_km": 10.0,
            "air_quality": {
                "pm2_5": 12.5
            }
        }
    }

def test_index_route(client):
    """Test the index route returns the search form"""
    with client.application.app_context():
        response = client.get('/')
        assert response.status_code == 200
        assert b'Get Weather Information' in response.data

@responses.activate
def test_weather_route_success(client, mock_weather_data, app):
    """Test successful weather data retrieval"""
    with app.test_request_context():
        with app.app_context():
            responses.add(
                responses.GET,
                app.config['WEATHER_API_URL'],
                json=mock_weather_data,
                status=200
            )

            response = client.post('/weather', data={'city': 'London'})
            assert response.status_code == 200
            assert b'Weather in London' in response.data
            assert b'Partly cloudy' in response.data

@responses.activate
def test_weather_route_error(client, app):
    """Test weather route with API error"""
    with app.test_request_context():
        with app.app_context():
            responses.add(
                responses.GET,
                app.config['WEATHER_API_URL'],
                json={"error": {"message": "API key not provided"}},
                status=401
            )

            response = client.post('/weather', data={'city': 'London'}, follow_redirects=True)
            assert response.status_code == 200
            assert b'Unable to fetch weather data' in response.data

def test_weather_route_invalid_form(client):
    """Test weather route with invalid form data"""
    response = client.post('/weather', data={'city': ''}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Please enter a city name' in response.data