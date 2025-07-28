import pytest
from flask import json

def test_get_data(client):
    """Test getting data from a protected endpoint."""
    login_response = client.post('/login', data=json.dumps({
        'username': 'testuser',
        'password': 'testpass'
    }), content_type='application/json')
    access_token = json.loads(login_response.data)['access_token']
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = client.get('/data', headers=headers)
    assert response.status_code == 200
    assert 'data' in json.loads(response.data)

def test_unauthorized_access(client):
    """Test access without authorization."""
    response = client.get('/data')
    assert response.status_code == 401