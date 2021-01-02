"""
Задание №6а
Реализовать скрипт-итератор, генерирующий целые числа, начиная с указанного.
Создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
"""

"""
Скрипт, генерирующий целые числа, начиная с указанного
"""

from sys import argv
try:
    file, start_num = argv
except ValueError:
    print("Неверные аргументы")
    exit()
from itertools import count
for i in count(int(start_num)):
    if i > 30:
        break
    else:
        print(i)