# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile
import pandas as pd

class Letters:

    stat = {}

    def __init__(self, zip_file_name):
        self.zip_file_name = zip_file_name

    def unzip(self):
        zip_file = zipfile.ZipFile(self.zip_file_name, "r")
        for filename in zip_file.namelist():
            zip_file.extract(filename)
        return filename

    def statistic(self, file_name):
        with open(file_name, "r", encoding="cp1251") as f:
            for line in f:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1

    def user_print(self):
        column = ["буква", "частота"]
        df = pd.DataFrame(data= self.stat.items(), columns= column)
        pd.set_option("display.max_rows", None)
        print(df.sort_values(by="частота", ascending= False))

letters = Letters(zip_file_name="voyna-i-mir.txt.zip")
letters.statistic(letters.unzip())
letters.user_print()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
