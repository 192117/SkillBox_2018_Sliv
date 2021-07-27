# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(self.name, other.name)
        elif isinstance(other, Fire):
            return Vapor(self.name, other.name)
        elif isinstance(other, Ground):
            return Dirt(self.name, other.name)
        else:
            return None

class Air:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Fire):
            return Flash(self.name, other.name)
        elif isinstance(other, Ground):
            return Vapor(self.name, other.name)
        elif isinstance(other, Water):
            return Storm(self.name, other.name)
        else:
            return None

class Fire:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Ground):
            return Lava(self.name, other.name)
        elif isinstance(other, Water):
            return Vapor(self.name, other.name)
        elif isinstance(other, Air):
            return Flash(self.name, other.name)
        else:
            return None

class Ground:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava(self.name, other.name)
        elif isinstance(other, Air):
            return Vapor(self.name, other.name)
        elif isinstance(other, Water):
            return Dirt(self.name, other.name)
        else:
            return None

class Storm:
    name = "Storm"

    def __init__(self, composite1, composite2):
        self.composite1 = composite1
        self.composite2 = composite2

    def __str__(self):
        return "{} + {} = {}".format(self.composite1, self.composite2, Storm.name)

class Vapor:
    name = "Vapor"

    def __init__(self, composite1, composite2):
        self.composite1 = composite1
        self.composite2 = composite2

    def __str__(self):
        return "{} + {} = {}".format(self.composite1, self.composite2, Vapor.name)

class Dirt:
    name = "Dirt"

    def __init__(self, composite1, composite2):
        self.composite1 = composite1
        self.composite2 = composite2

    def __str__(self):
        return "{} + {} = {}".format(self.composite1, self.composite2, Dirt.name)

class Flash:
    name = "Flash"

    def __init__(self, composite1, composite2):
        self.composite1 = composite1
        self.composite2 = composite2

    def __str__(self):
        return "{} + {} = {}".format(self.composite1, self.composite2, Flash.name)

class Dust:
    name = "Dust"

    def __init__(self, composite1, composite2):
        self.composite1 = composite1
        self.composite2 = composite2

    def __str__(self):
        return "{} + {} = {}".format(self.composite1, self.composite2, Dust.name)

class Lava:
    name = "Lava"

    def __init__(self, composite1, composite2):
        self.composite1 = composite1
        self.composite2 = composite2

    def __str__(self):
        return "{} + {} = {}".format(self.composite1, self.composite2, Lava.name)

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

water1 = Water('water')
fire1 = Fire('fire')
air1 = Air('air')
ground1 = Ground('ground')
print(water1 + fire1)

