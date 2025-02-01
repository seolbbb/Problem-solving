import math
t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    bound = int(m*n/math.gcd(m, n))
    k = x
    valid = 0
    while k <= bound:
        if (k-1)%m == (x-1) and (k-1)%n == (y-1):
            valid = 1
            break
        k += m

    if valid == 1:
        print(k)
    else:
        print(-1)