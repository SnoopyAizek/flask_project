import os

from decouple import config
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .views import views

db = SQLAlchemy()
toolbar = DebugToolbarExtension()
base_dir = os.path.dirname(__file__)
MIGRATE_REPO = os.path.join(base_dir, 'migrations')
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config('SECRET_KEY', cast=str)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASES', cast=str)
    app.register_blueprint(views, url_prefix='/')
    from app.api import views as api_views
    app.register_blueprint(api_views, url_prefix='/api')
    app.debug = config('DEBUG', cast=bool)
    db.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db, MIGRATE_REPO)
    from . import models
    return app
