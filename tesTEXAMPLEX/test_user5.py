import pytest


@pytest.mark.django_db
def test_new_user1(new_user1):
    print(new_user1.username)
    print(new_user1.first_name)
    print(new_user1.last_name)
    assert new_user1.username == 'hagp'
    assert new_user1.first_name == 'Aleksandr'


@pytest.mark.django_db
def test_new_user2(new_user2):
    print(new_user2.username)
    print(new_user2.first_name)
    print(new_user2.last_name)
    assert new_user2.username == 'hagp'
    assert new_user2.first_name == 'Aleksandr'
    assert new_user2.is_staff is True