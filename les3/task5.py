our_integer = int(input("Введите число: "))

if (our_integer % 2 == 0) and (sum(int(i) for i in str(our_integer)) % 3 == 0):
    print("Число", our_integer, "делится на 6")
else:
    print("Число", our_integer, "не делится на 6")