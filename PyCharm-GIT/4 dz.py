a = int(input("укажите первое число. a = "))
b = int(input("укажите второе число. b = "))
prib = int(input("введите прибавное число : "))

while a < b:
    a = a + prib;
    print("A + прибавное число = ", a, " < B = " , b)
    print('цикл окончен')

