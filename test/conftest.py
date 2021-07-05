from fastapi.testclient import TestClient
from pytest import fixture
from src.app import create_app


@fixture(scope="session")
def test_app():
    yield create_app()


@fixture(scope="session")
def test_client(app):
    yield TestClient(app)
