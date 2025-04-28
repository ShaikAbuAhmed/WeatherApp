import pytest
from app.forms import WeatherForm
from flask import Flask

def test_valid_weather_form(app):
    with app.test_request_context():
        form = WeatherForm(formdata=None)
        form.city.data = "London"
        assert form.validate() is True
        assert form.city.data == "London"

def test_empty_city_form(app):
    with app.test_request_context():
        form = WeatherForm(formdata=None)
        form.city.data = ""
        assert form.validate() is False
        assert "Please enter a city name" in form.city.errors

def test_city_name_too_short(app):
    with app.test_request_context():
        form = WeatherForm(formdata=None)
        form.city.data = "A"
        assert form.validate() is False
        assert "City name must be between 2 and 50 characters" in form.city.errors

def test_city_name_too_long(app):
    with app.test_request_context():
        form = WeatherForm(formdata=None)
        form.city.data = "A" * 51
        assert form.validate() is False
        assert "City name must be between 2 and 50 characters" in form.city.errors