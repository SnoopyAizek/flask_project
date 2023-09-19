import os
from datetime import timedelta

from decouple import config
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .views import views

db = SQLAlchemy()
toolbar = DebugToolbarExtension()
base_dir = os.path.dirname(__file__)
MIGRATE_REPO = os.path.join(base_dir, 'migrations')
migrate = Migrate()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config('SECRET_KEY', cast=str)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASES', cast=str)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = config('SECRET_KEY', cast=str)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    app.register_blueprint(views, url_prefix='/')
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    app.debug = config('DEBUG', cast=bool)
    db.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db, MIGRATE_REPO)
    jwt.init_app(app)
    from . import models
    return app
