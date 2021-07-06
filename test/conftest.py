from json import load

from fastapi.testclient import TestClient
from pytest import fixture
from src.app import create_app


@fixture(scope="session")
def test_app():
    yield create_app()


@fixture(scope="session")
def test_client(test_app):
    yield TestClient(test_app)


def load_test_data(api, dataset):
    file_path = f"test/data/{api}.json"

    with open(file_path, "r") as fp:
        data = load(fp)

        return data[dataset]
