from flask import jsonify

from app.api import views
from app.models import User


@views.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@views.route('/users', methods=['GET'])
def get_users():
    pass
