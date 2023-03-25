new_table_game = input('Введите новую игру: ')
games=[]
while new_table_game != "0":
    if new_table_game in games:
        print ('Эта игра уже есть в списке')
    else:
        games.append(new_table_game)
    new_table_game = input('Введите новую игру: ')
print('Cписок игр сформирован:')
games.sort()
print(games)