# 3. Запросить у пользователя ввод числа. Построить цикл от 0 до введённого числа (включительно) и
# для чётных чисел вывести то, что они чётные, а для нечётных, что они нечётные. Пример вывода:
#
# 0 is EVEN
# 1 is ODD
# 2 is EVEN
#
# и так далее...
from sys import float_info


def is_number_even():
    number = round(float(input('Enter a number: ')))
    # for num in range(number+1):
    #     if num % 2 == 0:
    #         print(num, "IS EVEN")
    #     else:
    #         print(num, "IS ODD")

    [print(num, "IS EVEN") if num % 2 == 0 else print(num, "IS ODD") for num in range(number+1)]

if __name__ == '__main__':
    is_number_even()