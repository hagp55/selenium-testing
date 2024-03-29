import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    user = User.objects.create_user('test', 'test@mail.com', 'test')
    print(User.objects.count())
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_create2():
    print(User.objects.count())
    assert User.objects.count() == 0