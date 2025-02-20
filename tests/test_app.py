import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_analytics_route(client):
    rv = client.get('/api/analytics')
    json_data = rv.get_json()
    assert 'status' in json_data