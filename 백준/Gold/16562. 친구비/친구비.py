import sys
input = sys.stdin.readline

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa != pb:
        parent[pa] = pb

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

n, m, k = map(int, input().split())
money = list(map(int, input().split()))
parent = [i for i in range(n+1)]
group_money = dict()
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n+1):
    cur_group = find(i)
    group_money[cur_group] = min(group_money.get(cur_group, 10000), money[i-1])

for x in group_money.values():
    ans += x

if k < ans:
    print('Oh no')
else:
    print(ans)