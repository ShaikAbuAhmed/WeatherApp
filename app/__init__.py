from flask import Flask
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_app(config_name='default'):
    """
    Application factory function that creates and configures the Flask app.
    
    Args:
        config_name (str): The configuration to use (development, production, or default)
    
    Returns:
        Flask: The configured Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    from config import config
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    csrf.init_app(app)
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app 