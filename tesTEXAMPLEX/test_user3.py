import pytest
from django.contrib.auth.models import User

# @pytest.fixture
# def user_1(db):
#     return User.objects.create_user('test')


# @pytest.mark.django_db
# def test_check_password(user_1):
#     user_1.set_password('new-password')
#     assert user_1.check_password('new-password') is True


@pytest.fixture
def user_1(db):
    user = User.objects.create_user('hagp', 'hagp@mail.ru', 'new-password')
    return user


@pytest.mark.django_db
def test_check_password(user_1):
    user = user_1
    assert user.username == 'hagp'
    assert user.email == 'hagp@mail.ru'
    assert user.check_password('new-password') is True