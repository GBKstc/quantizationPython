# app/__init__.py
from flask import Flask
from .config import Config
from .routes import api_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app
