"""
Задание №1
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
"""
Скрипт принимает 4 аргумента: название файла (file), выпаботку в часах (hours), ставку в час (sal_hour), 
премию (bonus). После этого производится расчет заработной платы сотрудника и вывод результата на экран.
В случае указания не всех параметров, производится остановка программы с выводом сообщения об ошибке
"""
from sys import argv
try:
    file, hours, sal_hour, bonus = argv
except ValueError:
    print("Неверные аргументы")
    exit()
salary = int(hours) * int(sal_hour) + int(bonus)
print(f"Заработная плата сотрудника: {salary}")
