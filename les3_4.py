# Решение1
# x = int(input("Введите чило для возведения в степень: "))
# y = int(input("Введите отрицательное чило, для возведения числа X в эту степень: "))
# if y <= 0:
#     x_y = x**y
#     print(x_y)
# else:
#     print("Введите отрицательное число! ")


# Решение 2

# def my_func():
#     x = float((input("Введите чило для возведения в степень: ")))
#     y = int(input("Введите отрицательное чило, для возведения числа X в эту степень: "))
#     if y <= 0:
#         return x**y
#     else:
#         return "Введите отрицательное число!"
#
#
# print(my_func())

# Решение 3
# def my_func(x, y):
#     result = 1
#     for i in range(abs(y)):
#         result *= x
#     if y >= 0:
#         return "Нужно отрицательное число!"
#     else:
#         return 1 / result
#
#
# print(my_func(float(input("Введите число 'X' для возведения в степень: ")),
#               int(input("Введите отрицательное чило, для возведения числа X в эту степень: "))))
