category = input()
if catefory =='Продукты':
    price = int(input())
    if price<100:
        print('Попробуйте нашу выпечку!')
    elif 100<=price<500:
        print("Как насчет орехов в шоколаде!")
    elif price<=500:
        print('Попробуйте экзотические фрукты!')
else: print('Загляните в товары для дома!')