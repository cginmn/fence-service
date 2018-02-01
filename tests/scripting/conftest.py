import pytest
from collections import OrderedDict

@pytest.fixture(scope='module')
def example_usernames():
    """Make a list of example usernames."""
    return ['A', 'B', 'C']


@pytest.fixture(scope='function', autouse=True)
def patch_driver(db, monkeypatch):
    """
    Change the database driver in ``fence.scripting.fence_create`` to use the
    one from the test fixtures.
    """
    monkeypatch.setattr(
        'fence.scripting.fence_create.SQLAlchemyDriver',
        lambda _: db,
    )


@pytest.fixture(scope='function', autouse=True)
def mock_keypairs(monkeypatch, kid, kid_2):
    """
    Change the keypair configuration in ``fence.settings.JWT_KEYPAIR_FILES``.
    """

    JWT_KEYPAIR_FILES = OrderedDict([
        (
            kid,
            ('tests/resources/keys/test_public_key.pem', 'tests/resources/keys/test_private_key.pem'),
        ),
        (
            kid_2,
            ('tests/resources/keys/test_public_key_2.pem', 'tests/resources/keys/test_private_key_2.pem'),
    ),
    ])

    monkeypatch.setattr(
        'fence.settings.JWT_KEYPAIR_FILES', JWT_KEYPAIR_FILES
    )