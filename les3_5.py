def my_func():
    sum_result = 0
    exit_code = False
    while exit_code == False:
        number = input("Введите числа для суммирования. Для выхода из программы, введите '№/#' ").split()

        result = 0
        for element in range(len(number)):
            if number[element] == '#' or number[element] == '№':
                exit_code = True
                break
            else:
                result = result + int(number[element])
        sum_result = sum_result + result
        print("Число, получившееся в итоге: ", sum_result)


my_func()
