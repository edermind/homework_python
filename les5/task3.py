marks = input('Введите свои оценки через пробел')
amount = len((marks.split(' ')))
five = marks.count('5')
print (f'Процент пятерок в твоих оценках: {100/amount*five}')