import math
r = float(input("Введите радиус цилиндра: "))
h = float(input("Введите высоту цилиндра: "))
V = round(math.pi * r**2 * h,1)
print("Объём цилиндра: ", V)