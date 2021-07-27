import random


def make_number():
    global number_make
    number_make = str(random.randint(1000, 9999))
    print(number_make)
    return number_make

def check_number(user_number):
    answer = {"bulls": 0, "cows": 0}
    for number in user_number:
        if number in number_make:
            if user_number.index(number) == number_make.index(number):
                answer["bulls"] += 1
            else:
                answer["cows"] += 1
    return answer

