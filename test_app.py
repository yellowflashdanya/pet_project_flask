import pytest
import os
from app.app import app as flask_app

os.environ["TESTING"] = "True"


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True

    with flask_app.test_client() as client:
        yield client


def test_homepage(client):
    response = client.get('/')

    assert response.status_code == 200

    assert b"Hello! I see you" in response.data
