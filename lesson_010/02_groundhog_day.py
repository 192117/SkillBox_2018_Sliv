# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

import random


ENLIGHTENMENT_CARMA_LEVEL = 777
carma_level = 0

class IamGodError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

class SuicideError(Exception):
    pass

def one_day():
    chance = random.randint(1, 13)
    print("chance =", chance)
    errors = [IamGodError("IamGodError"), DrunkError("DrunkError"),
              CarCrashError("CarCrashError"), GluttonyError("GluttonyError"),
              DepressionError("DepressionError"), SuicideError("SuicideError")]
    if chance == 13:
        try:
            raise random.choice(errors)
        except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exs:
            print('Ловим', exs)
    result = random.randint(1, 7)
    print("result =", result)
    return result


while carma_level < ENLIGHTENMENT_CARMA_LEVEL:
    carma_level += one_day()
    print("carma_level =", carma_level)


# https://goo.gl/JnsDqu
