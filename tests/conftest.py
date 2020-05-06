import pytest
from flask import Flask
from handlers.routes import configure_routes


@pytest.fixture(scope='module')
def create_app():
    app = Flask(__name__)
    configure_routes(app)
    return app.test_client()
