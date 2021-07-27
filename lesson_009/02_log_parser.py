# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile

class Parser:

    def __init__(self, file_name):
        self.file_name = file_name

    def save_file(self, name_output, includes):
        self.name_output = name_output
        with open(self.name_output, "a") as file1:
            file1.write(includes)

    def open_parser(self):
        count = 0
        time = "0"
        with open(self.file_name, "r", encoding="cp1251") as file:
            for line in file:
                line = line[:-1]
                if line.split(" ")[2] == "NOK":
                    if time != line.split(" ")[1][:5]:
                        if time != "0":
                            readlin = line.split(" ")[0] + " " + str(time) + "] " + str(count) + "\n"
                            self.save_file("result.txt", readlin)
                        time = line.split(" ")[1][:5]
                        count = 1
                    else:
                        count += 1


parser = Parser(file_name="events.txt")
parser.open_parser()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
