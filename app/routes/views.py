from flask import request, jsonify, render_template
from app import app, db
from app.models import User
from flask_jwt_extended import create_access_token, jwt_required

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(result="JWT is working!")

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404