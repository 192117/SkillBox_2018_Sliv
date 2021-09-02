# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

import os
from PIL import Image, ImageDraw, ImageFont

def make_ticket(fio, from_, to, date, file_name):
    picture = Image.open("D:\\Users\\Kokoc\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_013\\images\\ticket_template.png")
    imdraw = ImageDraw.Draw(picture)
    font = ImageFont.truetype("arial.ttf", size=18)
    imdraw.text((45, 120), fio, font=font, fill=ImageColor.colormap['black'])
    imdraw.text((45, 190), from_, font=font, fill=ImageColor.colormap['black'])
    imdraw.text((45, 258), to, font=font, fill=ImageColor.colormap['black'])
    imdraw.text((275, 258), date, font=font, fill=ImageColor.colormap['black'])
    picture.show()

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

make_ticket("Kalimullin Artur", "Saint-P", "SLV", "23/08/21")