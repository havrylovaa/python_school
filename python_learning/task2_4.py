# 4. Вы получаете ввод числа от пользователя.
#
# Построить цикл от 0 до введённого числа (включительно) и посчитать сумму всех чисел, делимых
# без остатка на 3 или 5. Вывести на консоль это число.
#
# Примечание: ❗️❗️❗️ задачу нужно решить как прямым for, так и с помощью list comprehension
def sum_of_numbers():
    number = int(input('Enter a number: '))
    # result = 0
    # for num in range(number + 1):
    #     if num % 3 == 0 or num % 5 == 0:
    #         result += num
    # print("sum of all numbers divisible by 3 or 5 is:", result)
    # вопрос:почему при отступе в последней строчке выводит результат на каждое число вместо итогового значения? как это работает?

    # result = sum(num for num in range(number + 1) if num % 3 == 0 or num % 5 == 0)
    result = sum(num for num in range(number + 1) if num % 3 == 0 or num % 5 == 0)
    print(result)

if __name__ == '__main__':
    sum_of_numbers()