T = int(input())

for i in range(T):
    H, W, N = map(int,input().split())
    a, b = divmod(N,H)
    if b == 0:
        print(100*H + a)
    else:
        print(100*b + a + 1)