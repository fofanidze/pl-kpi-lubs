#Перевірити, чи входить цифра 3 до складу заданого числа.

n1 = (input("n = "))
n2 = [int(d) for d in n1]
if 3 in n2:
    print("+")
else:
    print("-")