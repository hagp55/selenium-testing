import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_new_user1(user_factory):
    user = user_factory.build()
    # user = user_factory.create()
    user_cnt = User.objects.count()
    # print(f'{user_factory.username=}, {user_factory.is_staff=}')
    # print(user.username)
    assert user_cnt == 0




def test_new_user2(db, user_factory):
    # user = user_factory.build()
    user = user_factory.create()
    print(f'{user_factory.username=}, {user_factory.is_staff=}')
    print(user.username)
    assert True



@pytest.mark.django_db
def test_new_user3(new_user1):
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_product(product_factory):
    product = product_factory.build()
    print(product_factory.title)
    print(product_factory.description)
    assert True