import requests
from flask import current_app
from requests.exceptions import RequestException

class WeatherService:
    """
    Service class for handling weather API interactions.
    """
    
    @staticmethod
    def get_weather(city):
        """
        Get weather information for a given city.
        
        Args:
            city (str): Name of the city to get weather for
            
        Returns:
            dict: Weather data if successful, None if failed
            
        Raises:
            RequestException: If the API request fails
        """
        try:
            params = {
                'key': current_app.config['WEATHER_API_KEY'],
                'q': city,
                'aqi': 'yes'
            }
            
            current_app.logger.info(f"Making API request for city: {city}")
            
            response = requests.get(
                current_app.config['WEATHER_API_URL'],
                params=params,
                timeout=5
            )
            
            if response.status_code == 403:
                current_app.logger.error("API key is invalid or has expired")
                return None
                
            response.raise_for_status()
            
            data = response.json()
            
            if 'error' in data:
                current_app.logger.error(f"Weather API error: {data['error']['message']}")
                return None
                
            return data
            
        except RequestException as e:
            current_app.logger.error(f"Weather API request failed: {str(e)}")
            return None