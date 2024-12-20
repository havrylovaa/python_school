# 6. Дан список карт. Например, такой:
#
# current_hand = [2, 3, 4, 10, 'Q', 5]
#
# В общем и целом, список может содержать следующие значения: 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'.
#
# У каждой карты есть свой "вес":
#
# 2, 3, 4, 5, 6 весят +1
# 7, 8, 9 весят 0
# 10, 'J', 'Q', 'K', 'A' весят -1
# Задача: имея список карт, посчитать их общий "вес".
#
# Примеры входных данных и ожидаемых результатов:
#
# current_hand = [2, 3, 4, 10, 'Q', 5] # общий вес = 2
# current_hand = ['A', 3, 4, 10, 'J', 4] # общий вес = 0
# current_hand = [2, 7, 4, 9, 3, 5] # общий вес = 4
# Вычисленный общий вес карт записать в переменную с именем cards_sum
def calculate_card_sum():
    current_hand = [2, 3, 4, 10, 'Q', 5, 'a', 1]
    card_weights = {
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 0,
        8: 0,
        9: 0,
        10: -1,
        'J': -1,
        'Q': -1,
        'K': -1,
        'A': -1
    }
    cards_sum = 0
    for card in current_hand:
        if isinstance(card, str):
            cards_sum += card_weights[card.upper()]
        else:
            if card not in card_weights:
                print(f'{card} Не входит в список карт. Пожалуйста, веедите валидные значения')
            else:
                cards_sum += card_weights[card]

    print('Вес всех карт составляет: ', cards_sum)

if __name__ == '__main__':
    calculate_card_sum()
# сделать ручной ввод списка (каждый раз вводить символ)
# каким-то образом сделать так, чтобы цикл автомтически прекращался