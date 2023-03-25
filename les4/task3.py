login = input('Введите логин: ')
for symbol in '=?*^$№@_':
    if symbol in login:
        print('Вы использовали запрещенный символ:', symbol)