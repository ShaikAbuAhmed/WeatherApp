# Weather App

A Flask-based web application that provides real-time weather information using the WeatherAPI.com service.

## Features

- Real-time weather information display
- User-friendly interface
- Environment-based configuration
- Secure API key management
- Testing suite included

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/WeatherApp.git
cd WeatherApp
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY=your_secret_key
WEATHER_API_KEY=your_weather_api_key
```

## Running the Application

1. Activate the virtual environment (if not already activated)
2. Run the application:
```bash
python run.py
```
3. Open your browser and navigate to `http://localhost:5000`

## Testing

Run the test suite using pytest:
```bash
pytest
```

## Project Structure

```
WeatherApp/
├── app/                    # Application package
├── tests/                  # Test suite
├── .github/               # GitHub workflows
├── config.py              # Configuration settings
├── run.py                 # Application entry point
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Configuration

The application uses different configurations for development and production environments. The configuration is managed through the `config.py` file and environment variables.

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- WeatherAPI.com for providing the weather data API
- Flask framework and its extensions
- All contributors to this project 