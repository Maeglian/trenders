import pytest
from unittest.mock import patch
import os
from flask import url_for

TESTS_DIR = os.path.dirname(__file__)



@pytest.fixture
def trends_json():
    """
    Get dummy data from json
    :return: currency structure as string
    """
    path = os.path.join(TESTS_DIR, 'data/response.json')
    with open(path) as f:
        return f.read()

#@patch('trends.clients.google.get_trends_cached')
#def test_get_trends(mock_get, trends_json):
def test_get_trends()
    # mock_get.return_value = trends_json
    url = url_for('fetch')
    print(url)
    assert 0
