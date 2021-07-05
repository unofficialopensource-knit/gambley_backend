# Email send works fine
def test_send_email_pass(test_client):
    response = test_client.post(
        "/api/email/new",
        json={
            "sender": "string",
            "receiver": "string",
            "subject": "string",
            "template_id": 0,
            "template_params": {},
        },
    )

    assert response.status_code == 201
