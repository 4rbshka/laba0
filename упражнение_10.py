import math
a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))
sum = a + b
raz = a - b
proizv = a * b
chdel = a / b
ostdel = a % b
loga = math.log10(a)
step = a**b
print(" сумма = ",sum,"\n разность = ",raz,"\n произведение = ", proizv,
"\n деление = ", chdel , "\n остаток от деления = ", ostdel, "\n десятичный логарифм a = ", loga, "\n a в степени b = ", step)