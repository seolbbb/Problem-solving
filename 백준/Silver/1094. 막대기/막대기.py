x = int(input())
ans = 0

for i in range(7):
    if (x >> i) & 1:
        ans += 1

print(ans)