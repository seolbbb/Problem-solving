N, M = map(int, input().split())
basket = [0 for zero in range(N)]

for n in range(M):
    i, j, k = map(int, input().split())
    for p in range(j - i + 1):
        basket[i+p-1] = k

for x in basket:
    print(x, end = ' ')