# coding: utf-8

import os
import psutil
import shutil
import sys
import random


def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("File ", newfile, "has been successfully created")
            return True
        else:
            print("Houston, we have a problem!")
            return False


def sys_info():
    print("Вот что я знаю о системе")
    print("Количество процессоров: ", psutil.cpu_count())
    print("Платформа: ", sys.platform)
    print("Кодировка файловой системы: ", sys.getfilesystemencoding())
    print("Текущая директория: ", os.getcwd())
    print("Текущая пользователь: ", os.getlogin())


def del_dublicats(dirname):
    file_list = os.listdir(dirname)
   
    # Счетчик количества удаленных файлов    
    doubl_count = 0
    # Цикл for перебирает все значения из списка file_list
    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            # Делаем проверку, что файл не существует (т.е. был удален)
            if not os.path.exists(fullname):
                # Увеличиваем счетчик удаленных файлов
                doubl_count += 1
                print("Файл", fullname, "был успешно удален")
    return doubl_count


print("Welcome to GeekBrains python course")
print("Hello, %username%")

name = input("Your`s name: ")

print(name, ", welcome to my programm!")

# pep-8
answer = ''
while answer != 'Q':
    answer = input("Would you like to work with me? (Y/N/Q)  ")
        
    if answer == 'Y':
        print("So, i can:")
        print(" [1] - display a list of files")
        print(" [2] - display info about system")
        print(" [3] - display list of processes")
        print(" [4] - duplicate files in the current directory")
        print(" [5] - duplicate mark files in the current directory")
        print(" [6] - remove files in current directory")

        do = int(input("Choose number: "))
        
        if do == 1:
            print(os.listdir())

        elif do == 2:
        	sys_info()
            
        elif do == 3:
            print(psutil.pids())
            
        elif do == 4:
            print("Make files duplicate")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                duplicate_file(file_list[i])
                i += 1

        elif do == 5:
            print("duplicate mark files in the current directory")
            filename = input("Write file name:")
            duplicate_file(filename)

        elif do == 6:
            print("Delete duplicates")
            dirname = input("Directory name is:")
            count = del_dublicats(dirname)
            print("Files delete: ", count)

        else:
            pass

    elif answer == 'N':
        print("Good by, my darling!")
    else:
        print("Are you stupid?")
