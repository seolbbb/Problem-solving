N, M = map(int, input().split())
basket = [i+1 for i in range(N)]

for m in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]

print(*basket)