s = int(input("s = "))
hours = s // 3600
minutes = (s // 60) % 60
sec = s % 60
print(f"{hours}h {minutes} m {sec} s")