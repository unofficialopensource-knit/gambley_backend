from pytest import mark

from src.dependencies import fast_mail
from .conftest import load_test_data


# Test for all cases of validation errors 422
@mark.parametrize("test_data", load_test_data("email", "invalid_request"))
def test_send_email_fails_request_validation(test_client, test_data):
    response = test_client.post("/api/email/new", json=test_data["payload"])

    assert response.status_code == 422

    response_data = response.json()
    assert isinstance(response_data["detail"], list)
    assert test_data["invalid_attribute"] in response_data["detail"][0]["loc"]


# Test email is sent 202 status code
@mark.parametrize("test_data", load_test_data("email", "success"))
def test_send_email_passes(test_client, test_data):
    fast_mail.config.SUPPRESS_SEND = 1

    with fast_mail.record_messages() as outbox:
        response = test_client.post("/api/email/new", json=test_data["payload"])

        assert response.status_code == 202

        response_data = response.json()
        assert "receiver" in response_data.keys()
        assert isinstance(response_data["receiver"], list)
        assert len(response_data["receiver"]) == len(test_data["payload"]["receiver"])

        assert len(outbox) == len(test_data["payload"]["receiver"])

        for index, item in enumerate(outbox):
            assert item["To"] == test_data["payload"]["receiver"][index]
