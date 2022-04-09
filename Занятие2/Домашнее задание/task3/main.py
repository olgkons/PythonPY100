а = int(input("введите число  "))
b = int(input("введите число  "))
c = int(input("введите число  "))

uslovie1 = a < 45 and b >= 45 and c >= 45
uslovie2 = a >= 45 and b < 45 and c >= 45
uslovie3 = a >= 45 and b >= 45 and c < 45
if uslovie1 or uslovie2 or uslovie3:
    print("одно из чисел  меньше 45")
else:
    print("Все числа больше 45 или все числа меньше 45")
