A, B = map(int, input().split())
C = B - 45

if A != 0:
    if C < 0:
        print((A-1), (60+C))
    else:
        print(A, C)
else:
    if C < 0:
        print(23, (60+C))
    else:
        print(A, C)