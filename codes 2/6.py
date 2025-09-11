lst = []
lst_size = 20



for i in range(lst_size):
    while True:
        try:
            num = input(f'Введіть число {i+1}: ')
            number = int(num)
            lst.append(number)
            break
        except ValueError:
            print("poshel v zhopy")

print("\nVAsh masiv: ", lst)