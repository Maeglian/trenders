import pytest
from trends.app import create_app


@pytest.fixture
def app():
    app = create_app(None, is_start_get_trends=False)
    return app


