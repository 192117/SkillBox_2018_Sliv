# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!

# TODO тут ваш код в многопоточном стиле

import threading
import os
import csv

def parser_directory(directorys, data):
    for file_directorys in os.walk(directorys):
        os.chdir(directorys)
        for file in file_directorys[2]:
            data.append(file)

class Volatility(threading.Thread):

    def __init__(self, file, directory, lock1, lock2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file
        self.directory = directory
        self.traders = dict()
        self.traders_lock = lock1
        self.traders_zero = dict()
        self.traders_zero_lock = lock2

    def run(self):
        os.chdir(self.directory)
        for traders in self.file:
            with open(traders) as file_traders:
                file_csv = csv.reader(file_traders, delimiter=",")
                max_price = 0
                min_price = 0
                next(file)
                for row in file_csv:
                    secid = row[0]
                    price = float(row[2])
                    if price > max_price:
                        if min_price == 0:
                            min_price = price
                        max_price = price
                    elif price < min_price:
                        min_price = price
                medium_price = (max_price + min_price) / 2
                volatility = ((max_price - min_price) / medium_price) * 100
                if volatility > 0.0:
                    self.traders_lock.acquire()
                    self.traders[secid] = float(format(volatility, ".2f"))
                    self.traders_lock.release()
                else:
                    self.traders_zero_lock.acquire()
                    self.traders_zero[secid] = float(format(volatility, ".2f"))
                    self.traders_zero_lock.release()

if __name__ == "__main__":
    os.chdir("C:\\Users\\kalimullin\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades")
    base_data = list()
    parser_directory("C:\\Users\\kalimullin\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades", base_data)
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    volatility = [Volatility(file=file,
                      directory="C:\\Users\\kalimullin\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades",
                      lock1=lock1, lock2=lock2) for file in base_data]
    for vol in volatility:
        vol.start()
    for vol in volatility:
        vol.join()

