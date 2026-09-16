# import pytest

# from restaurant_booking import create_booking, calculate_price, apply_discount

# @pytest.fixture
# def booking():
#     return create_booking("Emi", 2)

# def test_create_booking():
#     booking = create_booking("Emi", 2)

#     assert booking["name"] == "Emi"
#     assert booking["people"] == 2

# def test_create_booking_empty_name():
#     with pytest.raises(ValueError):
#         create_booking("", 2)

# def test_create_booking_zero_people():
#     with pytest.raises(ValueError):
#         create_booking("Emi", 0)

# def test_create_booking_negative_people():
#     with pytest.raises(ValueError):
#         create_booking("Emi", -1)

# @pytest.mark.parametrize("people, hour, expected_price", [
#     (1, 17, 1000),
#     (2, 17, 2000),
#     (3, 18, 4500),
#     (4, 20, 6000),
# ])
# def test_calculate_price(people, hour, expected_price):
#     assert calculate_price(people, hour) == expected_price

# def test_apply_discount_regular(booking):
#     booking["vip"] = False
#     price = apply_discount(booking, 2000)

#     assert price == 2000

# def test_apply_discount_vip(booking):
#     booking["vip"] = True
#     price = apply_discount(booking, 2000)

#     assert price == 1600

# def test_booking_fixture(booking):
#     assert booking["name"] == "Emi"
#     assert booking["people"] == 2
