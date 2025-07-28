from app.database import db
from app.models.user import User

class UserService:
    def create_user(self, data):
        user = User(username=data['username'], password=data['password'])  # Password should be hashed in production
        db.session.add(user)
        db.session.commit()
        return user.to_dict()