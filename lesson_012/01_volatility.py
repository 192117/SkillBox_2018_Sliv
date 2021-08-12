# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
import os
import csv
from utils import time_track

class Volatility:

    def __init__(self):
        self.traders = dict()
        self.traders_zero = dict()
        self.data = list()


    def trader_sort_volat(self, trader, reverse=True):
        sort_traders = sorted(list(trader.items()), key=lambda x: x[1], reverse=reverse)
        return sort_traders[:3]


    def trader_sort_without(self, trader):
        sort_traders = sorted(list(trader.items()), key=lambda x: x[0], reverse=False)
        return sort_traders


    def see_result(self):
        print("Максимальная волатильность:")
        for value in self.trader_sort_volat(self.traders):
            print(value[0], "--", value[1], "%")
        print("Минимальная волатильность:")
        for value in self.trader_sort_volat(self.traders, reverse=False):
            print(value[0], "--", value[1], "%")
        print("Нулевая волатильность:")
        rows = ""
        for value in self.trader_sort_without(self.traders_zero):
            rows += value[0] + ", "
        print(rows)


    def make_data(self):
        for file_directory in os.walk("D:\\Users\\Kokoc\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades"):
            os.chdir("D:\\Users\\Kokoc\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades")
            for traders_file in file_directory[2]:
                self.data.append(traders_file)

    def run(self):
        os.chdir("D:\\Users\\Kokoc\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades")
        for traders_file in self.data:
            with open(traders_file) as file:
                file_csv = csv.reader(file, delimiter=",")
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
                    self.traders[secid] = float(format(volatility, ".2f"))
                else:
                    self.traders_zero[secid] = float(format(volatility, ".2f"))
        self.see_result()

@time_track
def main():
    voland = Volatility()
    voland.make_data()
    voland.run()

if __name__=="__main__":
    main()

# data = ["TICKER_AFH9.csv", "TICKER_AFM9.csv", "TICKER_ALH9.csv", "TICKER_ALM9.csv", "TICKER_VIH9.csv"]
# os.chdir("D:\\Users\\Kokoc\\PycharmProjects\\SkillBox_2018_Sliv\\lesson_012\\trades")
# traders = dict()
# traders_zero = dict()
# for data_file in data:
#     with open(data_file) as f:
#         file = csv.reader(f, delimiter=",")
#         max_price = 0
#         min_price = 0
#         next(file)
#         for row in file:
#             secid = row[0]
#             price = float(row[2])
#             if price > max_price:
#                 if min_price == 0:
#                     min_price = price
#                 max_price = price
#             elif price < min_price:
#                 min_price = price
#         medium_price = (max_price + min_price) / 2
#         volatility = ((max_price - min_price) / medium_price) * 100
#         if volatility > 0.0:
#             traders[secid] = float(format(volatility, ".2f"))
#         else:
#             traders_zero[secid] = float(format(volatility, ".2f"))
# print(traders)
# print(traders_zero)
# sort_traders = sorted(list(traders.items()), key= lambda x: x[1], reverse=True)
# print(sort_traders)
# print(sort_traders[:3])
# print(sort_traders[-3:])
