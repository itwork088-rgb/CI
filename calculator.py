def add(a, b):
    return a + b


# def discount_price(price, percent):
#     if price < 0 or percent < 0 or percent > 100:
#         raise ValueError("Некорректные данные")
#     return price * (1 - percent / 100)

# def is_adult(age):
#     return age >= 18

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b