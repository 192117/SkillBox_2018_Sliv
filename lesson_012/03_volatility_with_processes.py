# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/02_volatility_with_threads.py !!!

# TODO тут ваш код в многопроцессном стиле

from multiprocessing import Process, Pipe
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


class Volatility(Process):

    def __init__(self, file, directory, conn, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file
        self.directory = directory
        self.conn = conn

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
                self.conn.send([secid, float(format(volatility, ".2f"))])
                self.conn.close()
            else:
                self.conn.send([secid, float(format(volatility, ".2f"))])
                self.conn.close()

@time_track
def main():
    os.chdir("D:\\Users\\Kokoc\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades")
    base_data = list()
    parser_directory("D:\\Users\\Kokoc\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades", base_data)
    tr = dict()
    tr_zero = dict()
    pipes, volaty = [], []
    for file in base_data:
        parent_conn, child_conn = Pipe()
        volatility = Volatility(file=file,
                                directory="D:\\Users\\Kokoc\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades",
                                conn=child_conn)
        pipes.append(parent_conn)
        volaty.append(volatility)

    for vol in volaty:
        vol.start()

    for conn in pipes:
        trad, value = conn.recv()
        if value != 0.0:
            if trad not in tr:
                tr[trad] = value
        else:
            if trad not in tr_zero:
                tr_zero[trad] = value

    for vol in volaty:
        vol.join()

    see_result(tr, tr_zero)

if __name__ == "__main__":
    main()