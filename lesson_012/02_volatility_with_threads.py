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
from utils import time_track

def parser_directory(directorys, data):
    for file_directorys in os.walk(directorys):
        os.chdir(directorys)
        for file in file_directorys[2]:
            data.append(file)


def trader_sort_volat(trader, reverse=True):
    sort_traders = sorted(list(trader.items()), key=lambda x: x[1], reverse=reverse)
    return sort_traders[:3]


def trader_sort_without(trader):
    sort_traders = sorted(list(trader.items()), key=lambda x: x[0], reverse=False)
    return sort_traders


def see_result(tr11, tr11_zero):
    print("Максимальная волатильность:")
    for value in trader_sort_volat(tr11):
        print(value[0], "--", value[1], "%")
    print("Минимальная волатильность:")
    for value in trader_sort_volat(tr11, reverse=False):
        print(value[0], "--", value[1], "%")
    print("Нулевая волатильность:")
    rows = ""
    for value in trader_sort_without(tr11_zero):
        rows += value[0] + ", "
    print(rows)


class Volatility(threading.Thread):

    def __init__(self, file, directory, data_trader, data_trader_zero, lock1, lock2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file
        self.directory = directory
        self.data_trader = data_trader
        self.data_trader_zero = data_trader_zero
        self.traders_lock = lock1
        self.traders_zero_lock = lock2

    def run(self):
        with open(self.file) as file_traders:
            file_csv = csv.reader(file_traders, delimiter=",")
            max_price = 0
            min_price = 0
            next(file_traders)
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
                if secid not in self.data_trader:
                    self.data_trader[secid] = float(format(volatility, ".2f"))
                self.traders_lock.release()
            else:
                self.traders_zero_lock.acquire()
                if secid not in self.data_trader_zero:
                    self.data_trader_zero[secid] = float(format(volatility, ".2f"))
                self.traders_zero_lock.release()

@time_track
def main():
    os.chdir("D:\\Users\\Kokoc\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades")
    base_data = list()
    parser_directory("D:\\Users\\Kokoc\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades", base_data)
    tr = dict()
    tr_zero = dict()
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    volatility = [Volatility(file=file,
                      directory="D:\\Users\\Kokoc\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades",
                      lock1=lock1, lock2=lock2, data_trader=tr, data_trader_zero=tr_zero) for file in base_data]
    for vol in volatility:
        vol.start()
    for vol in volatility:
        vol.join()

    see_result(tr, tr_zero)

if __name__ == "__main__":
    main()