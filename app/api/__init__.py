from flask import Blueprint

views = Blueprint('api', __name__)
from app.api import users
