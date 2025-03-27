n = int(input())
lst = list(input().split('0'))
marble = []
m = 0
ans = 0

for i in range(n+1):
    m += i
    marble.append(m)

for base in lst:
    ans += marble[len(base)]

print(ans)