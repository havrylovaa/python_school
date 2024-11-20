def derevo():
    size = int(input('Введите размер елки: '))
    for item in range(1, size+1, 2):
        print('*' * item)

if __name__ == '__main__':
    derevo()