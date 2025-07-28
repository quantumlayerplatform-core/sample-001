from .models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

class UserRepository:
    def create_user(self, username, email, password):
        password_hash = generate_password_hash(password)
        user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def verify_user(self, username, password):
        user = self.get_user_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            return True
        return False