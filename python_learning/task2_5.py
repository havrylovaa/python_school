# 5. На вход подаются два списка чисел длины N.
#
# Задача: взять из первого списка все нечётные числа, из второго чётные и объединить их в новом списке с названием joined_list.
#
# Примечание:❗️❗️❗️ задачу нужно решить как прямым for, так и с помощью list comprehension

def joined_list():
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = [7, 8, 9, 10, 11, 12]
    # joined_list = []
    # for num in first_list:
    #     if num % 2 == 1:
    #         joined_list.append(num)
    # for num in second_list:
    #     if num % 2 == 0:
    #         joined_list.append(num)
    # print(joined_list)

    join_list = [num for num in first_list if num % 2 == 1] + [num for num in second_list if num % 2 == 0]
    print(join_list)

if __name__ == '__main__':
    joined_list()