# Решение 1
# name_user = input("You name? ")
# surname_user = input("You surname? ")
# year_born_user = input("You year of birth? ")
# city_live_user = input("What city in u live? ")
# email_user = input("What it u email? ")
# number_telephone_user = input("What it u telephone number? ")
#
#
# def info_user(**kwargs):
#     return kwargs
#
#
# input(print(info_user(name=name_user, surname=surname_user, year_born=year_born_user, city_live=city_live_user,
#                       email=email_user, number_telephone=number_telephone_user)))


# Решение 2
def info_user(**kwargs):
    return kwargs


input((dict(info_user(name=input("Ваше имя: ")), surname=input("Ваша фамилия: "),
            year_born=int(input("год рождения (Например : 1998): ")),
            city_live=input("В каком городе проживаете: "), email=input("Ваша электронная почта: "),
            number_telephone=int(input("Ваш номер телефона: ")))))
