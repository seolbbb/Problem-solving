import sys
input = sys.stdin.readline

n, m = map(int,input().split())
tree = list(map(int,input().split()))
low, high = (1, max(tree))

while high >= low:
    total = 0
    mid = (high + low) // 2

    for i in range(n):
        if tree[i] >= mid:
            total += tree[i] - mid

    if total >= m:
        low = mid + 1
    elif total < m:
        high = mid - 1

print(high)