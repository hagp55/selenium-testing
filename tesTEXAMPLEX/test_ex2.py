import pytest


@pytest.fixture(scope='session')
def connect_to_db():
    print('******Connected to database******')
    yield 'yes'
    print('******Disconnected database******')



@pytest.fixture(scope='function')
def fixture1():
    print('\nrun-fixture with scope function\n')
    return 1


@pytest.mark.skip
def test_ex2(connect_to_db, fixture1):
    print('\ntext from print in test_ex2\n')
    num = fixture1
    assert num == 1


def test_ex3fixture1(connect_to_db, fixture1):
    print('\ntext from print in test_ex3\n')
    num = fixture1
    assert num == 1


def test_ex4(fixture1):
    print('\ntext from print in test_ex4\n')
    num = fixture1
    assert num == 1