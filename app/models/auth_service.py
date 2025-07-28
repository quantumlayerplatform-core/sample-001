import jwt
import datetime
from app.models.user import User

class AuthService:
    def authenticate(self, credentials):
        user = User.query.filter_by(username=credentials['username']).first()
        if user and user.password == credentials['password']:  # Password should be hashed and checked in production
            token = jwt.encode({
                'sub': user.id,
                'iat': datetime.datetime.utcnow(),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }, 'your_secret_key', algorithm='HS256')
            return token
        return None