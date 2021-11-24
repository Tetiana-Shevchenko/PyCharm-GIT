import random
nums=list(range(1, 11))
random.shuffle(nums)
kos=nums[:10]
print(kos)
print("Номер числа 7 в этом списке:")
print(kos.index(7) + 1)




