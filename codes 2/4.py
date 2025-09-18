#Вивести перші (n) чисел кратних 7 (де (n) вводить користувач).

n = int(input("n = "))
for i in range(n):
    if i % 7 == 0 and i != 0:
        print(i)
