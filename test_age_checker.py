from age_checker import is_adult


def test_is_adult():
    assert is_adult(20) is True

def test_not_adult():
    assert is_adult(16) is False