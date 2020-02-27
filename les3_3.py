# Решение 1


# user_input1 = int(input("Введите первое число: "))
# user_input2 = int(input("Введите второе число: "))
# user_input3 = int(input("Введите третье число: "))
# my_func = [user_input1, user_input2, user_input3]
# my_func.sort()
# tuple(my_func)
# number_one = my_func[-1]
# number_two = my_func[-2]
# number_three = number_two + number_one
# print(number_three, "сумма самых больших чисел)")


# Решение 2



# def my_func(argument_1, argument_2, argument_3):
#     if argument_1 >= argument_3 and argument_2 >= argument_3:
#         return argument_1 + argument_2
#     elif argument_1 > argument_2 and argument_1 < argument_3:
#         return argument_1 + argument_3
#     else:
#         return argument_2 + argument_3
#
#
# print(
#     f'Результат - {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')
