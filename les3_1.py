# Решение №1

# user_dividend = float(input("Введите делимое: "))
# user_divider = float(input("Введите делитель: "))
#
#
# def my_func(dividend, divider):
#     dividend = user_dividend
#     divider = user_divider
#     if divider == 0:
#         print("Режим самоучничтожения активирован!")
#     else:
#         return dividend / divider
#
#
# print(my_func(user_dividend, user_divider))

# Решение №2


# def my_func():
#     user_dividend = float(input("Введите делимое: "))  # сделал флоат для большей вариативности
#     user_divider = float(input("Введите делитель: "))  # сделал флоат для большей вариативности
#     if user_divider == 0:
#         # print("Режим самоучничтожения активирован!") - если отставить так , в результат выпадает None из 2 части
#         # функции
#         return "Самоуничтожение запущено)"
#     else:
#         return user_dividend / user_divider
#
#
# print(my_func())

# Решение 3

# def my_func(user_dividend, user_divider):
#     if user_divider == 0:
#         return "Самоуничтожение запущено)"
#     else:
#         return user_dividend / user_divider
#
#
# print(my_func(int(input("Введите делимое: ")),
#               int(input("Введите делитель: "))))
