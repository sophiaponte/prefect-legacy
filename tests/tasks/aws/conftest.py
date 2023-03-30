import pytest


@pytest.fixture(autouse=True)
def clear_client_cache():
    from prefectlegacy.utilities.aws import _CLIENT_CACHE

    _CLIENT_CACHE.clear()
