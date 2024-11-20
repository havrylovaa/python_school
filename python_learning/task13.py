# Задание 3: Удаление элементов из множества
# Дано множество и список элементов, которые нужно удалить из этого множества. Необходимо удалить указанные элементы и вернуть результат.
# original_set = {"apple", "banana", "cherry", "date", "fig"}
# items_to_remove = ["banana", "date"]
def task13():
    original_set = {"apple", "banana", "cherry", "date", "fig"}
    items_to_remove = ["banana", "date"]
    for item in items_to_remove:
        original_set.remove(item)
    #     можно также использоать discard что исключит ошибку если во втором подмножестве будут слова, которых нет в первом подмножестве
    # print(original_set)
    return original_set

if __name__ == "__main__":
    print(task13())