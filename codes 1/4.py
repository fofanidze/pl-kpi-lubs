n = int(input("n =  "))

for i in range(2, n+1):
    for d in range(2, i):
        if i % d == 0:
            break
    else:
        print(i)