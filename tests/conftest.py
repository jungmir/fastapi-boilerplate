import os
import pytest

from fastapi.testclient import TestClient
from server.common.create_app import app_generator

@pytest.fixture(scope='session')
def app():
    os.environ['API_TEST'] = 'test'
    return app_generator()

@pytest.fixture(scope='session')
def client(app):
    return TestClient(app=app)


@pytest.fixture(scope='class')
def global_settings(request, client):
    client = client
    request_url = 'http://localhost:8000'
    
    request.cls.settings = dict(client=client, request_url=request_url)
    yield