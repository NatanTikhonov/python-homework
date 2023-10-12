def chet():
    n = input("Введите любое целое число: ")
    try:
        n = float(n)
        if n % 1 == 0:
            n = int(n)
            if n % 2 == 0:
                print("Число " + str(n) + " чётное")
            else:
                print("Число " + str(n) + " нечётное")
        else:
            print("Вы ввели нецелое число. Как можно быть настолько тупорылым?")
            chet()
    except:
        print("Что непонятного во фразе ЛЮБОЕ ЦЕЛОЕ ЧИСЛО?")
        chet()

chet()