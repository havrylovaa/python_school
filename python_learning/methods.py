def methods_print():
    # s ='hello'.upper()
    # print(s)
    # t = 'WORLD'.lower()
    # print(t)
    # print(type(t))
    s = 'Hello world'
    # s = s.upper()
    # print(s)
    # print(s.count('L'))
    # print(s.count('l',6))
    # print(s.find('e'))
    # print(s.rfind('o'))
    # print(s.index('w'))
    # print(s.replace('o','a'))
    # print(s.replace('l', ' ', 2))
    # print(s.isalpha())
    # print('fjedjfdlksj'.isalpha())
    # print('1234'.isdigit())
    # d = "123"
    # p = d.rjust(5, "O")
    # print(p)
    txt = input("Введите ваше ФИО: ").lower()
    print (txt.split('А'))
    # print(len(txt.split()))
    # print('12,34637,38367,8283'.split(','))
    # t = ('12', '34637', '38367', '8283')
    # print(('+'.join(t)))
    print('+'.join(txt.split('а')))


methods_print()