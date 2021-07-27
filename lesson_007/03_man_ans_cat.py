# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint
# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def take_cat(self, cat):
        self.cat = cat.name
        cat.house = self.house
        cprint('{} приютил себе {}'.format(self.name, self.cat), color='cyan')

    def buy_food_cat(self):
        if self.house.money > 50:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cats_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_house(self):
        cprint('{} убираюсь за котом!'.format(self.name), color='red')
        if (self.house.cats_dirt - 100) <=0:
            self.house.cats_dirt = 0
        else:
            self.house.cats_dirt -= 100
        self.fullness -= 50

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 8)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cats_food < 20:
            self.buy_food_cat()
        elif self.house.cats_dirt > 50:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class Cat:

    def __init__(self, name):
        self.name = name
        self.house = None
        self.fullness = 50

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cats_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cats_food -= 10
        else:
            cprint('{} нет еды для кота'.format(self.name), color='red')

    def sleep(self):
        cprint('{} пошел спать'.format(self.name), color='red')
        self.fullness -= 10

    def make_dirt(self):
        cprint('{} шкодничаю'.format(self.name), color='cyan')
        self.fullness -= 10
        self.house.cats_dirt += 5

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 4)
        if self.fullness < 20:
            self.eat()
        elif self.house.cats_food < 20:
            self.make_dirt()
        elif dice == 1:
            self.sleep()
            self.sleep()
            self.sleep()
        elif dice == 3:
            self.make_dirt()
            self.eat()
            self.make_dirt()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cats_food = 0
        self.cats_dirt = 0

    def __str__(self):
        return 'В доме осталось еды для человека {} , для кота {} , денег осталось {} , грязи {}'.format(
            self.food, self.cats_food, self.money, self.cats_dirt)

my_sweet_home = House()
pets = Cat("Бублик")
citisen = Man("Вадим")
citisen.go_to_the_house(my_sweet_home)
citisen.take_cat(pets)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    citisen.act()
    print('--- в конце дня ---')
    print(citisen)
    print(pets)
    print(my_sweet_home)
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
