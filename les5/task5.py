# Напишите программу проверяющую является ли список чисел возрастающим непрерывно.
# Например для списка [0,1,2,3,4], программа должна выводить “Да”, а для списка [0,1,3,4] “Нет”.
# Для последовательности из 1 числа программа должна писать “Нет”.

first_list = [0,1,2,3,4]
second = [0,1,3,4]

our_list = [int(x) for x in input().split()]
if len(our_list) == 1:
    print("Нет")
else:
    for i in range(len(our_list) - 1):
        if our_list[i] >= our_list[i+1]:
            print("Нет")
            break
    else:
        print("Да")