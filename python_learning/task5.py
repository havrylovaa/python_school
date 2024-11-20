# INT, FLOAT
# Задание 5: Сумма и произведение цифр числа
#
# Дано целое число:
# number = 12345
#
# Найдите сумму всех цифр числа.
# Найдите произведение всех цифр числа.
# Ожидаемый результат: Отобразите сумму и произведение цифр числа.
def task5():
    number = 12345
    sum = 0
    # while number != 0:
    #     last_item_removed = number % 10
    #     sum += last_item_removed
    #     number = number // 10
    # print('Sum', sum)
    # prod = 1
    # while number > 0:
    #     digit = number % 10
    #     prod *= digit
    #     number = number // 10
    # print('Prod', prod)
    prod = 1
    while number > 0:
        digit = number % 10
        sum += digit
        prod *= digit
        number //= 10
    print ('Sum', sum)
    print('Prod', prod)


if __name__ == '__main__':
    task5()
