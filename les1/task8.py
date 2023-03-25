number = int(input('Введите трехзначное число: '))
first = number//100
second = number//10-first*10
third = number-number//10*10
print (sum([first,second,third]))