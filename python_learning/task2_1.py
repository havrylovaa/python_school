# Измените код так, чтобы вывод соответствовал тексту в комментариях.
# x = "My name is Agent Smith"
# # y
# # nesgt
from dataclasses import replace

from faker.utils.decorators import lowercase


def task2_1():
    x = "My name is Agent Smith"
    updated_string = x.split('S')[0]
    y = updated_string[3::3]
    print(y)

if __name__ == "__main__":
    task2_1()