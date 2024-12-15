N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    print("Case #{}: {}".format(i + 1, a + b))