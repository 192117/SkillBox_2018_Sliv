# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


class Parser:

    def __init__(self, file_name):
        self.file_name = file_name

    def open_parser(self):
        count = 0
        time = "0"
        with open(self.file_name, "r", encoding="cp1251") as file:
            for line in file:
                line = line[:-1]
                if line.split(" ")[2] == "NOK":
                    if time != line.split(" ")[1][:5]:
                        if time != "0":
                            readlin = line.split(" ")[0] + " " + str(time) + "] " + str(count)
                            yield readlin
                        time = line.split(" ")[1][:5]
                        count = 1
                    else:
                        count += 1


parser = Parser(file_name="events.txt").open_parser()
print(parser)
for value in parser:
    print(value)