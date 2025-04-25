from flask import Blueprint, render_template, flash, redirect, url_for
from app.forms import WeatherForm
from app.services.weather_service import WeatherService

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    """Render the home page with the weather form."""
    form = WeatherForm()
    return render_template('index.html', form=form)

@main.route('/weather', methods=['POST'])
def weather():
    """Handle weather form submission and display results."""
    form = WeatherForm()
    
    if not form.validate_on_submit():
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{getattr(form, field).label.text}: {error}", 'error')
        return redirect(url_for('main.index'))
    
    weather_data = WeatherService.get_weather(form.city.data)
    
    if not weather_data:
        flash('Unable to fetch weather data. Please try again.', 'error')
        return redirect(url_for('main.index'))
    
    return render_template('weather.html', weather=weather_data) 