from fastapi.testclient import TestClient
from pytest import fixture
from src.app import create_app


@fixture(scope="session")
def test_app():
    yield create_app()


@fixture(scope="session")
def test_client(test_app):
    yield TestClient(test_app)
