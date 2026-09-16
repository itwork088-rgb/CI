# import pytest

# from cart import item_count, total_price, dif_items, buy


# @pytest.fixture
# def cart_items():
#     return [
#         {"name": "Book", "price": 100, "quantity": 2},
#         {"name": "Pen", "price": 50, "quantity": 1},
#     ]


# def test_total_price(cart_items):
#     assert total_price(cart_items) == 250


# def test_item_count(cart_items):
#     assert item_count(cart_items) == 3


# def test_dif_items(cart_items):
#     assert dif_items(cart_items) == 2


# def test_dif_items_second(cart_items):
#     assert dif_items(cart_items) != 3


# @pytest.fixture
# def user():
#     return {
#         "name": "Emiliya",
#         "is_active": True,
#         "balance": 1000,
#     }


# def test_buy_success(user):
#     assert buy(user, 500) is True

# def test_buy_not_enough_balance(user):
#     with pytest.raises(ValueError):
#         buy(user, 1500)

# def test_buy_inactive_user(user):
#     user["is_active"] = False
#     with pytest.raises(ValueError):
#         buy(user, 500)
