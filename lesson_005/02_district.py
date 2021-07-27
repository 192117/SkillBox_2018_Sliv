# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as house1_room1
from district.central_street.house1 import room2 as house1_room2
from district.central_street.house2 import room1 as house2_room1
from district.central_street.house2 import room2 as house2_room2
from district.soviet_street.house1 import room1 as sovet_house1_room1
from district.soviet_street.house1 import room2 as sovet_house1_room2
from district.soviet_street.house2 import room1 as sovet_house2_room1
from district.soviet_street.house2 import room2 as sovet_house2_room2

print('На centrall street живут', house1_room1.folks + house1_room2.folks + house2_room1.folks + house2_room2.folks)
print('На soviet street живут', sovet_house1_room1.folks + sovet_house1_room2.folks +
      sovet_house2_room1.folks + sovet_house2_room2.folks)
