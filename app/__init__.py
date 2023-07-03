from flask import Flask
from .views import views
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from flask_debugtoolbar import DebugToolbarExtension


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config('SECRET_KEY', cast=str)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASES', cast=str)
    app.register_blueprint(views, url_prefix='/')
    app.debug = config('DEBUG', cast=bool)
    db = SQLAlchemy(app)
    toolbar = DebugToolbarExtension(app)
    return app
