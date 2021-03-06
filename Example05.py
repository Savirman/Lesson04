"""
Задание №5
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

"""
Программа формирует список из четных чисел в диапазоне от 100 до 1000 (включая границы) с помощью генератора.
Затем произовится умножение всех элементов получившегося списка с выводом результата
"""

new_list = [el for el in range(100, 1000) if el % 2 == 0]
print(new_list)

from functools import reduce
total_mult = reduce(lambda x, y: x * y,new_list)
print(total_mult)