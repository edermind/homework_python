width = float(input('Введите ширину поверхности: '))
height = float(input('Введите высоту поверхности: '))
consp = int(input('Введите расход краски кв.м/л: '))
volume = int(input('Введите объем банки: '))
reserve = int(input('Введите процент запаса: '))

space = width * height
amount_litr = (space / consp) * (reserve/100) + (space / consp)
amount_can = amount_litr // volume + 1

print (round(space,2))
print (round(amount_litr,2))
print (amount_can)
print (round(amount_can*volume - amount_litr,2))