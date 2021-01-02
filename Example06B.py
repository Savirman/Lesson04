"""
Задание №6б
Реализовать скрипт-итератор, повторяющий элементы некоторого списка, определенного заранее.
Создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
"""
Скрипт, повторяющий элементы списка num_list задаваемое пользователем колчество раз (count)
"""

from sys import argv
try:
    file, count = argv
except ValueError:
    print("Неверные аргументы")
    exit()
num_list = [1, 3, 6, 7, 2, 12, 65]
len_of_num = len(num_list)
from itertools import cycle
iter = 0
for item in cycle(num_list):
    if iter >= len_of_num * int(count):
        break
    print(item)
    iter += 1