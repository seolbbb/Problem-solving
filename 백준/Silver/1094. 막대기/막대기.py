x = int(input())
ans = 0

for i in range(6, -1, -1):
    k = 2 ** i
    if x >= k:
        x -= k
        ans += 1

print(ans)