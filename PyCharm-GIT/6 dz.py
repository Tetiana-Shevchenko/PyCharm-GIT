import random

length = int(input("Введите длину списка: "))
list = ""
i = 0
while i < length:
    n = str(random.randint(0, 9))
    list = list + n + ", "
    i +=1
5
print(list)