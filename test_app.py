import pytest
import app as my_app_module

@pytest.fixture
def client():
  test_app = my_app_module.app

  test_app.config['TESTING'] = True

  with test_app.test_client() as client:
    yield client

def test_homepage(client):
  response = client.get('/')

  assert response.status_code == 200

  assert b"Hello! I see you" in response.data