from django.test.client import Client
from django.urls import reverse


def test_app_session_gone(db, user):
    # intentionally use a vanilla Django test client
    client = Client()
    # Force login, creates a Django session
    client.force_login(user)
    # That Django session should not play any role.
    resp = client.get(
        reverse("headless:app:current_session"), HTTP_X_SESSION_TOKEN="gone"
    )
    assert resp.status_code == 410


def test_logout(auth_client, headless_reverse):
    # That Django session should not play any role.
    resp = auth_client.get(headless_reverse("headless:current_session"))
    assert resp.status_code == 200
    resp = auth_client.delete(headless_reverse("headless:current_session"))
    assert resp.status_code == 401
    resp = auth_client.get(headless_reverse("headless:current_session"))
    assert resp.status_code == 401
