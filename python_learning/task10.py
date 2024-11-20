# Подсчет частоты слов
#
# У вас есть строка, содержащая несколько слов. Необходимо создать словарь, где ключами будут слова, а значениями — количество раз, сколько каждое слово встречается в строке.
#
# text = "apple banana apple orange banana apple orange apple"
#
# Разбейте строку на слова и подсчитайте количество вхождений каждого слова.
# Выведите словарь с результатами подсчета.
# Отсортируйте словарь по количеству вхождений слов в порядке убывания. Если два слова встречаются одинаковое количество раз, отсортируйте их в алфавитном порядке.
def task10():
    text = "apple banana apple orange banana apple orange apple"
    # words = text.split(' ')
    # dict_words_count = {}
    # for word in words:
    #     if word in dict_words_count:
    #         dict_words_count[word] += 1
    #     else:
    #         dict_words_count[word] = 1
    #
    #
    # print(dict_words_count)
    #
    # sorted_dict_words_counts = (sorted(dict(dict_words_count.items(), key=lambda item: (-item[1], item[0]))))
    # print(sorted_dict_words_counts)
    words_unique = set(text.split())
    dict_words_count = {}
    for word in words_unique:
        count = 0
        for item in list(text.split(' ')):
            if item == word:
                count += 1
        dict_words_count[word] = count
    print(dict_words_count)
# Для сортировки словаря используем функцию sorted(), которая сортирует элементы по ключу. Мы передаем в неё функцию lambda, которая сортирует сначала по количеству вхождений (в порядке убывания, поэтому используем отрицательное значение -item[1]), а затем по алфавиту (по умолчанию алфавитная сортировка идет по возрастанию).
# new_dict_words_count_list = dict(sorted(word_count[item])
# использовать SET()
# двумя способами через sorted и как-то по-другому


if __name__ == '__main__':
    task10()
