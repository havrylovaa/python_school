# 2. Вывести лесенкой (как половина ёлки) символ звёздочки по кол-ву строк, заданных пользователем:
# запросить ввод у пользователя кол-ва строк, вывести звёздочки лесенкой.
# - Например, пользователь ввёл число 4. Тогда выводим:
def derevo():
    size = int(input('Введите размер елки: '))
    for item in range(1, size+1):
        print('*' * item)

if __name__ == '__main__':
    derevo()