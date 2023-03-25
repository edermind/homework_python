command = input()
if command =='game':
    print ('Играем в игру угодай число, у тебя 3 попытки')
    for i in range(3):
        number = int(input())
        if number == 5:
            print ('Вы выиграли')