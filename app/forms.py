from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class WeatherForm(FlaskForm):
    """
    Form for submitting city name to get weather information.
    """
    city = StringField(
        'City Name',
        validators=[
            DataRequired(message='Please enter a city name'),
            Length(min=2, max=50, message='City name must be between 2 and 50 characters')
        ],
        render_kw={"placeholder": "Enter city name", "class": "form-control"}
    )
    submit = SubmitField('Get Weather', render_kw={"class": "btn btn-primary"}) 