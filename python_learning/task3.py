# text = "Python programming is fun!"
#
# Подсчитайте количество букв в строке (без учёта пробелов и знаков пунктуации).
# Найдите количество гласных букв в строке.
# Замените все пробелы символом "-".
# Ожидаемый результат: Отобразите количество букв в строке, количество гласных и строку с заменёнными пробелами.
def task3():
    text = 'Python programming is fun!'
    # new_list = []
    # for item in text:
    #     if item.isalpha():
    #         new_list.append(item)
    # print(len(new_list))
    # vowels = 'aeiouyAEIOUY'
    # new_list2 = []
    # for item in text:
    #     if item in vowels:
    #         new_list2.append(item)
    # print(len(new_list2))
    # print(text.replace(" ", "-"))
    vowels = 'aeiouyAEIOUY'
    new_list = len([item for item in text if item.isalpha()])
    print(new_list)
    new_list2 = len([item for item in text if item in vowels])
    print(new_list2)
    print((text.replace(" ", "-")))



if __name__ == '__main__':
    task3()
