#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append('Artur')
my_family.append('Father')
my_family.append('Mother')

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
]

my_family_height.append(['Artur', 178])
my_family_height.append(['Father', 170])
my_family_height.append(['Mother', 170])

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("Height's father -", my_family_height[1][1], "см")

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print("Height's ours family - ", my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1], "см")

print(my_family)
print(my_family_height)