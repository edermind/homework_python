number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
amount = (number_3+number_2+number_1)
sale = (amount/2)
if number_2>number_1 and number_3>number_2:
    print ("Акция!", sale)
elif number_2<number_1 and number_3<number_2:
    print ("Акция!", sale)
else: print('К оплате',amount)