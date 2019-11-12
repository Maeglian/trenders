import os
import uuid

import pytest
from sqlalchemy_utils import create_database, drop_database
from yarl import URL

TESTS_DIR = os.path.dirname(__file__)
DATABASE_URL = os.getenv('DATABASE_URL',
                         'postgresql://me:hackme@0.0.0.0/citizens')


@pytest.fixture
def temp_db() -> str:
    tmp_db_name = '.'.join([uuid.uuid4().hex, 'pytest'])
    tmp_db_url = str(URL(DATABASE_URL).with_path(tmp_db_name))
    create_database(tmp_db_url)

    try:
        yield tmp_db_url
    finally:
        drop_database(tmp_db_url)


@pytest.fixture
def trends_json():
    """
    Get dummy data from json
    :return: currency structure as string
    """
    path = os.path.join(TESTS_DIR, 'data/response.json')
    with open(path) as f:
        return f.read()
