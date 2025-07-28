import pytest
from models import User

def test_create_user(init_database):
    """Test creating a user in the database."""
    user = User(username='testuser', password='hashed_password')
    init_database.session.add(user)
    init_database.session.commit()
    assert user in init_database.session