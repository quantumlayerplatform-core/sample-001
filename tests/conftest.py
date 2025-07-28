import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

@pytest.fixture(scope='module')
def app():
    """Create and configure a new app instance for each test."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret_key'
    return app

@pytest.fixture(scope='module')
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture(scope='module')
def init_database():
    """Initializes the database for the test session."""
    db = SQLAlchemy()
    db.create_all()
    yield db
    db.drop_all()
    db.session.commit()