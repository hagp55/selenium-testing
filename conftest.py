import pytest
from pytest_factoryboy import register

from tesTEXAMPLEX.factories import CategoryFactory, ProductFactory, UserFactory

register(UserFactory)
register(CategoryFactory)
register(ProductFactory)


@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create()
    return user
