# Задание 4: Проверка палиндрома
#
# Напишите программу, которая проверяет, является ли строка палиндромом. Палиндром — это строка,
# которая читается одинаково как слева направо, так и справа налево.
#
# Пример строки:
# word = "madam"
# text = "Уж редко рукою окурок держу"
# Преобразуйте строку к нижнему регистру и удалите все пробелы.
# Проверьте, является ли строка палиндромом.
# Ожидаемый результат: Отобразите сообщение о том, является ли строка палиндромом или нет.
def task4():
    n = -1
    # text = input("Введите строку: ")
    text = "madam"
    updated_text = text.replace(" ", "").lower()
    # if text1 == text1[::-1]:
    #     print("Строка палиндромна")
    # else:
    #    print("Строка не палиндромна")
    for item in updated_text:
        if item == updated_text[n]:
            n = n - 1
            if n < -len(updated_text):
                print("Строка является палидромом")
        else:
            print("Строка не является палиндромом")
    # print(text.replace(" ", "").lower())


if __name__ == '__main__':
    task4()
