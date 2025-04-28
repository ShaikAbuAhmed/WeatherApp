# Building a Weather Dashboard with Flask & GitHub Copilot

A demonstration of modern Python web development workflow using GitHub Copilot.

## 1. Prerequisites & Initial Setup

### Environment Setup
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

### Copilot-Assisted Code Generation
```text
Prompt: "Create a Flask weather dashboard that uses WeatherAPI.com. Include routes for home and weather lookup"
```

### Initial Project Structure
```
weather_app/
├── app/
│   ├── __init__.py      # Flask application factory
│   ├── routes.py        # Application routes
│   └── templates/       # Jinja2 templates
├── tests/
│   ├── __init__.py
│   └── test_app.py      # Test suite
├── .env                 # Environment variables
├── config.py           # Configuration settings
└── run.py             # Application entry point
```

## 2. Debugging Scenarios

### Common Error: Invalid API Key
```python
# Original .env
WEATHER_KEY=abc123  # Incorrect variable name

# Fixed .env
WEATHER_API_KEY=abc123  # Correct variable name
```

### Error Resolution Steps
```bash
# Test API connection
curl -X GET "http://api.weatherapi.com/v1/current.json?key=$WEATHER_API_KEY&q=London"

# Verify environment variables
python -c "import os; print(os.getenv('WEATHER_API_KEY'))"
```

## 3. Test Suite Implementation

### Running Tests
```bash
pytest -v --cov=app --cov-report=term-missing
```

### Sample Test Case
```python
def test_weather_endpoint(client):
    response = client.get('/weather?city=London')
    assert response.status_code == 200
    assert b'Weather for London' in response.data
```

## 4. CI/CD Integration

### GitHub Actions Workflow
```yaml
name: Python CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
      - name: Run Tests
        run: |
          pip install -r requirements.txt
          pytest
```

## 5. Development Workflow

### Branch Management
```bash
git checkout -b feature/weather-endpoint
git add .
git commit -m "Add weather endpoint with API integration"
git push origin feature/weather-endpoint
```

### Pull Request Process
- Create PR via GitHub UI
- Request review from team members
- Address feedback and merge

## 6. Next Steps

- [ ] Add caching for API responses
- [ ] Implement user location detection
- [ ] Add historical weather data
- [ ] Create Docker deployment configuration

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [WeatherAPI Docs](https://www.weatherapi.com/docs/)
- [GitHub Actions](https://docs.github.com/en/actions)

For detailed setup instructions and API documentation, see the [Wiki](./wiki).