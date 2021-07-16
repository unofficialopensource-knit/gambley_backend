from json import load
from os import environ

from fastapi.testclient import TestClient
from pytest import fixture
from src.app import create_app


@fixture(scope="session")
def test_app():
    environ["GAMBLEY_SUPRESS_SEND"] = "1"
    environ["GAMBLEY_MAIL_USERNAME"] = "test_user"
    environ["GAMBLEY_MAIL_USERNAME"] = "test_password"
    yield create_app()


@fixture(scope="session")
def test_client(test_app):
    yield TestClient(test_app)


def load_test_data(api, dataset):
    file_path = f"test/data/{api}.json"

    with open(file_path, "r") as fp:
        data = load(fp)

        return data[dataset]
