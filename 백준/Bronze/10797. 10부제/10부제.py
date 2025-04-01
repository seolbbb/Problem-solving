num = int(input())
car = list(map(int, input().split()))
ans = 0

for n in car:
    if n == num:
        ans += 1

print(ans)