while True:
    income = int(input())
    if income == 0:
        break

    if income <= 1000000:
        print(income)
    elif income <= 5000000:
        print(int(income*0.9))
    else:
        print(int(income*0.8))
