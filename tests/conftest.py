import pytest

from backend.application import create_app


@pytest.fixture(scope="session")
def test_client():
    flask_app = create_app(config_name="test")
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client
