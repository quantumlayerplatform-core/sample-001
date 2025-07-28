from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.services.auth_service import AuthService

user_blueprint = Blueprint('user', __name__)
user_service = UserService()
auth_service = AuthService()

@user_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = user_service.create_user(data)
    return jsonify(user), 201

@user_blueprint.route('/login', methods=['POST'])
def login():
    credentials = request.get_json()
    token = auth_service.authenticate(credentials)
    if token:
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401