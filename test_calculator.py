# import pytest

# from calculator import add, discount_price, is_adult
# from calculator import multiply, subtract

# def test_multiply():
#     assert multiply(2, 3) == 6


# def test_subtract():
#     assert subtract(5, 3) == 2

# def test_subtract_negative():
#     assert subtract(3, 5) == -2


# @pytest.mark.parametrize(
#     "a, b, expected",
#     [
#         (1, 2, 3),

#         (10, 20, 30),
#         (-1, -2, -3),
#         (0, 5, 5),
#     ],
# )
# def test_add(a, b, expected):
#     assert add(a, b) == expected


# @pytest.mark.parametrize(
#     "price, percent, expected",
#     [
#         (100, 0, 100),
#         (100, 10, 90),
#         (100, 100, 0),
#     ],
# )
# def test_discount_price(price, percent, expected):
#     assert discount_price(price, percent) == expected


# @pytest.mark.parametrize(
#     "price, percent",
#     [
#         (-1, 10),
#         (100, -1),
#         (100, 101),
#     ],
# )
# def test_discount_price_rejects_invalid_data(price, percent):
#     with pytest.raises(ValueError):
#         discount_price(price, percent)


# @pytest.mark.parametrize(
#     "age, expected",
#     [   
#         (0, False),
#         (17, False),
#         (18, True),
#         (30, True),
#     ],
# )
# def test_is_adult(age, expected):
#     assert is_adult(age) == expected 

from calculator import add, multiply, subtract, divide

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(2, 3) == 6

def test_subtract():
    assert subtract(5, 3) == 2

def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False
    except ValueError:
        assert True
