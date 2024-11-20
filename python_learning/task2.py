# Задание
# 2: Работа со строками в списке
# Дан список строк:
# words = ["apple", "banana", "avocado", "grape", "kiwi"]
# Найдите все слова, которые начинаются с букв "a".
# Преобразуйте эти слова в верхний регистр.
# Выведитеколичество слов, начинающихся на букву "a", и новый список с преобразованными словами.
# Ожидаемый результат: Отобразите список слов, начинающихся с "a", в верхнем регистре, и их количество.

def task2():
    words = ["apple", "banana", "avocado", "grape", "kiwi"]
    # words1 = [i.upper() for i in words]

    # for i in words:
    #     if i.startswith("a"):
    #         result.append(i)
    # print(result)
    # result1 = [i.upper() for i in result]
    new_list = [i.upper() for i in words if i.startswith("a")]
    for i in words:
        if i.startswith("a"):
            i.upper()

    print(len(new_list))

task2()

if __name__ == '__main__':
    task2()