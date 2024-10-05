a = int(input("Введите целое число от 1 до 1000: "))
if a > 1000 or a < 1:
    print("Ты уверен?")
else:
    b = a%9; b1 = a//9; c = b1%9; c1 = b1//9; d = c1%9; d1 = c1//9; e = d1%9;
print(e, d, c, b, sep='')