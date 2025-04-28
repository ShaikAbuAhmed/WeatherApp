import pytest
import responses
from app.services.weather_service import WeatherService
from flask import current_app

@pytest.fixture
def mock_weather_response():
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

@responses.activate
def test_get_weather_success(app, mock_weather_response):
    with app.app_context():
        # Mock the API response
        responses.add(
            responses.GET,
            f"{current_app.config['WEATHER_API_URL']}",
            json=mock_weather_response,
            status=200
        )
        
        # Test the weather service
        result = WeatherService.get_weather("London")
        
        assert result is not None
        assert result["location"]["name"] == "London"
        assert result["current"]["temp_c"] == 15
        assert result["current"]["condition"]["text"] == "Partly cloudy"

@responses.activate
def test_get_weather_api_error(app):
    with app.app_context():
        # Mock API error response
        responses.add(
            responses.GET,
            f"{current_app.config['WEATHER_API_URL']}",
            json={"error": {"code": 1002, "message": "API key not provided."}},
            status=401
        )
        
        # Test the weather service with error
        result = WeatherService.get_weather("London")
        assert result is None

@responses.activate
def test_get_weather_network_error(app):
    with app.app_context():
        # Mock network error
        responses.add(
            responses.GET,
            f"{current_app.config['WEATHER_API_URL']}",
            body=Exception("Connection error")
        )
        
        # Test the weather service with network error
        result = WeatherService.get_weather("London")
        assert result is None