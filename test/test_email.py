from pytest import mark

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
