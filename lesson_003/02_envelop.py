# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper = [(8, 9), (9, 8), (6, 8), (8, 6), (3, 4), (11, 9), (9, 11)]
# paper_x, paper_y = 8, 9
# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)
for paper_x, paper_y in paper:
    if paper_y * paper_x <= envelop_x * envelop_y:
        print('Yes')
    else:
        print('No')
print('-------')
# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
brick = [(11, 10, 2), (11, 2, 10), (10, 11, 2), (10, 2, 11), (2, 10, 11), (2, 11, 10), (3, 5, 6), (3, 6, 5), (6, 3, 5),
         (6, 5, 3), (5, 6, 3), (5, 3, 6), (11, 3, 6), (11, 6, 3), (6, 11, 3), (6, 3, 11), (3, 6, 11), (3, 11, 6)]
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)

for brick_x, brick_y, brick_z in brick:
    if brick_x < hole_x and (brick_y < hole_y or brick_z < hole_y) \
            or brick_x < hole_y and (brick_y < hole_x or brick_z < hole_x) \
            or brick_y < hole_x and (brick_x < hole_y or brick_z < hole_y) \
            or brick_y < hole_y and (brick_x < hole_x or brick_z < hole_x) \
            or brick_z < hole_x and (brick_x < hole_y or brick_y < hole_y) \
            or brick_z < hole_y and (brick_x < hole_x or brick_y < hole_x):
        print('Yes')
    else:
        print('No')
