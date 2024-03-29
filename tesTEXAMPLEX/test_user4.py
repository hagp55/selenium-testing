import pytest


@pytest.mark.django_db
def test_check_password1(user_1):
    user = user_1
    assert user.username == 'hagp'
    assert user.email == 'hagp@mail.ru'
    assert user.check_password('new-password') is True


@pytest.mark.django_db
def test_check_password2(user_1):
    user = user_1
    assert user.username == 'hagp'
    assert user.email == 'hagp@mail.ru'
    assert user.check_password('new-password') is True