while True:
    X = list(map(int, input().split()))
    if 0 in X:
        break
    X.sort()
    if X[0]**2 + X[1]**2 == X[2]**2:
        print('right')
    else:
        print('wrong')