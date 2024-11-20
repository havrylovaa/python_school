# Подсчет количества встречающихся элементов
#
# У вас есть словарь, где ключами являются имена, а значениями — списки покупок.
# Необходимо подсчитать, сколько раз каждый товар встречается в списках.
#
# shopping_lists = {
#     "Alice": ["apple", "banana", "orange"],
#     "Bob": ["banana", "milk", "orange"],
#     "Charlie": ["apple", "milk", "bread"]
# }
# Создайте новый словарь, где ключами будут товары, а значениями — количество их встречаемости во всех списках.
# Выведите получившийся словарь.
def task9():
    shopping_lists = {
        "Alice": ["apple", "banana", "orange"],
        "Bob": ["banana", "milk", "orange"],
        "Charlie": ["apple", "milk", "bread"]
    }
    new_list = {}
    for items in shopping_lists.values():
        for item in items:
            if item in new_list:
                new_list[item] += 1
            else:
                new_list[item] = 1
    print(new_list)

if __name__ == '__main__':
    task9()