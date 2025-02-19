import sys
input = sys.stdin.readline

n = int(input())
budget_list = sorted(list(map(int, input().split())))
budget = int(input())
prefix = [0 for _ in range(n+1)]
ans = 0

for i in range(1, n+1):
    prefix[i] = prefix[i-1] + budget_list[i-1]

if budget >= sum(budget_list):
    ans = max(budget_list)
else:
    for i in range(0, n):
        cap = (budget-prefix[i]) // (n-i)
        ans = max(ans, cap)

print(ans)