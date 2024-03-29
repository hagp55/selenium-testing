import pytest


def test_example1():
    # print('test1')
    assert 1 == 1


def test_example2():
    assert 1 == 1


@pytest.mark.skip('temporary skip')
def test_wrong_example1():
    assert 1 == 2


@pytest.mark.xfail
def test_wrong_example2():
    assert 1 == 2


@pytest.mark.slow
def test_slow_action():
    assert 1 == 1