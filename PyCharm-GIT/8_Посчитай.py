n = int(input())

suma = 0
mult = 1

while n > 0:
    digit = n % 10
    suma = suma + digit
    n //= 10
print("Сумма:", suma)



