from flask import Flask
from app.handlers.user_handler import user_blueprint
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.database import db

def create_app():
    app = Flask(__name__)
    
    # Configuration for the Flask app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(user_blueprint)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)