# TUPLE
# Задание 7: Объединение кортежей и нахождение максимального значения
#
# Даны два кортежа:
# tuple1 = (1, 3, 5, 7)
# tuple2 = (2, 4, 6, 8)
#
# Объедините оба кортежа в один.
# Найдите максимальное значение в объединённом кортеже.
# Ожидаемый результат: Отобразите объединённый кортеж и максимальное значение.
def task7():
    tuple1 = (1, 3, 5, 7)
    tuple2 = (2, 4, 6, 8)
    tuple3 = tuple1 + tuple2
    max_value = max(tuple3)
    print(tuple3, "\n", max_value)

if __name__ == '__main__':
    task7()