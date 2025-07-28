import pytest
from flask import json

def test_register_user(client):
    """Test user registration."""
    response = client.post('/register', data=json.dumps({
        'username': 'testuser',
        'password': 'testpass'
    }), content_type='application/json')
    assert response.status_code == 200
    assert 'access_token' in json.loads(response.data)

def test_login_user(client):
    """Test user login."""
    response = client.post('/login', data=json.dumps({
        'username': 'testuser',
        'password': 'testpass'
    }), content_type='application/json')
    assert response.status_code == 200
    assert 'access_token' in json.loads(response.data)