# def create_booking(name, people):
#     if not name:
#         raise ValueError("имя не может быть пустым")
#     if people < 1:
#         raise ValueError("количество людей должно быть больше 1")

#     return {
#         "name": name,
#         "people": people,
#     }


# def calculate_price(people, hour):
#     if hour < 18:
#         return people * 1000
#     else:
#         return people * 1500


# def apply_discount(booking, price):
#     if booking["vip"]:
#         return price * 0.8

#     return price
