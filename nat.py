def year():
    y = input("Введите любое натуральное число: ")
    try:
        y = int(y)
        if y <= 0:
            print("Необходимо ввести НАТУРАЛЬНОЕ число")
            year()
        if (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0):
            print("YES")
        else:
            print("NO")
    except:
        print("Вы ввели неверные данные. Попробуйте ещё разок")
        year()

year()