while True:
    x = input()
    y = 0

    if int(x) == 0:
        break

    for i in range(len(x)//2):
        if x[i] != x[-i-1]:
            print('no')
            y = 1
            break
    if y == 0:
        print('yes')