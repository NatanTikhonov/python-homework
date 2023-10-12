def sign():
    x = input("Введите любое десятичное число: ")
    try:
        x = float(x)
        if x < 0:
            sign_x = -1
            print(sign_x)
        elif x == 0:
            sign_x = 0
            print(sign_x)
        else:
            sign_x = 1
            print(sign_x)
    except:
        print("Может, тебе стоит сдавать обществознание и историю?")
        sign()

sign()