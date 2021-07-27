# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass

class NotEmailError(Exception):
    pass

class Register():

    def __init__(self, file_name):
        self.file_name = file_name

    def write_file(self, outfile, info):
        with open(outfile, "a", encoding="UTF8") as f:
            f.write(info)

    def check_line(self, line):
        try:
            if len(line.split(" ")) == 3:
                try:
                    if line.split(" ")[0].isalpha():
                        try:
                            if line.split(" ")[1].find("@") != -1 or line.split(" ")[1].find(".") != -1:
                                try:
                                    if 10 <= int(line.split(" ")[2]) <= 99:
                                        self.write_file("registrations_good.log", line)
                                    else:
                                        raise ValueError
                                except ValueError as ex:
                                    self.write_file("registrations_bad.log", (line[:-1] + f" Ошибка {type(ex)}\n"))
                            else:
                                raise NotEmailError
                        except NotEmailError as ex:
                            self.write_file("registrations_bad.log", (line[:-1] + f" Ошибка {type(ex)}\n"))
                    else:
                        raise NotNameError
                except NotNameError as ex:
                    self.write_file("registrations_bad.log", (line[:-1] + f" Ошибка {type(ex)}\n"))
            else:
                raise ValueError
        except ValueError as ex:
            self.write_file("registrations_bad.log", (line[:-1] + f" Ошибка {type(ex)}\n"))


    def work_with_file(self):
        with open(self.file_name, "r", encoding="UTF8") as file:
            for line in file:
                self.check_line(line)


reg = Register("registrations.txt")
reg.work_with_file()