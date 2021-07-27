# -*- coding: utf-8 -*-

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import os
import shutil
import time
import zipfile

class PhotoSort:

    def __init__(self, file_name):
        self.file_name = file_name

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name + ".zip", 'r')
        zfile.extractall()

    def make_dir(self):
        outfile_name = self.file_name + "_by_year"
        os.mkdir(outfile_name)

    def foto(self):
        for i in os.walk("icons"):
            for j in os.walk(os.path.abspath(i[0])):
                for k in j[2]:
                    os.chdir("D:\\Browser's Download\\[SkillBox] [Вадим Шандринов] Python-разработчик\\9. Работа с файлами и форматированный вывод\\lesson_009\\icons_by_year")
                    try:
                        os.mkdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[0]))
                        os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[0]))
                        try:
                            os.mkdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[1]))
                            os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[1]))
                            try:
                                os.mkdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[2]))
                                os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[2]))
                                shutil.copy2(os.path.join(j[0], k), os.getcwd())
                            except OSError:
                                os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[2]))
                                shutil.copy2(os.path.join(j[0], k), os.getcwd())
                        except OSError:
                            os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[1]))
                            try:
                                os.mkdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[2]))
                                os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[2]))
                                shutil.copy2(os.path.join(j[0], k), os.getcwd())
                            except OSError:
                                os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[2]))
                                shutil.copy2(os.path.join(j[0], k), os.getcwd())
                    except OSError:
                        os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[0]))
                        try:
                            os.mkdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[1]))
                            os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[1]))
                            try:
                                os.mkdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[2]))
                                os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[2]))
                                shutil.copy2(os.path.join(j[0], k), os.getcwd())
                            except OSError:
                                os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[2]))
                                shutil.copy2(os.path.join(j[0], k), os.getcwd())
                        except OSError:
                            os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[1]))
                            try:
                                os.mkdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[2]))
                                os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[2]))
                                shutil.copy2(os.path.join(j[0], k), os.getcwd())
                            except OSError:
                                os.chdir(str(time.gmtime(os.path.getmtime(os.path.join(j[0], k)))[2]))
                                shutil.copy2(os.path.join(j[0], k), os.getcwd())


shot = PhotoSort(file_name="icons")
shot.unzip()
shot.make_dir()
shot.foto()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
