# def total_price(items):
#     return sum(item["price"] * item["quantity"] for item in items)


# def item_count(items):
#     return sum(item["quantity"] for item in items)


# def dif_items(items):
#     names = []

#     for item in items:
#         names.append(item["name"])
#     return len(names)

# def buy(user, price):
#     if not user["is_active"]:
#         raise ValueError("User is not active")
#     if user["balance"] < price:
#         raise ValueError("Not enough balance")
#     user["balance"] -= price
#     return True
