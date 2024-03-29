import pytest
from django.contrib.auth.models import User


@pytest.fixture
def prepare_user_fixture():
    User.objects.create_user('test', 'test@mail.ru', 'test')


@pytest.mark.django_db
def test_create_user1(prepare_user_fixture):
    User.objects.create_user('test2', 'test@mail.ru', 'test')
    print(User.objects.all())
    count = User.objects.count()
    assert count == 2


@pytest.mark.django_db
def test_create_user2(prepare_user_fixture):
    count = User.objects.count()
    print(User.objects.all())
    assert count == 1