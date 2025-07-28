from flask import request, jsonify
from .repositories import UserRepository
from .models import db

app = Flask(__name__)
user_repository = UserRepository()

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return jsonify({'error': 'Missing data'}), 400
    user = user_repository.create_user(username, email, password)
    return jsonify({'id': user.id, 'username': user.username}), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if user_repository.verify_user(username, password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)