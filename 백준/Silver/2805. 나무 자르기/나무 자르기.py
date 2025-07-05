import sys
inpur = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))
tree = 0
left = 0
right = max(height)

while left <= right:
    mid = (left + right) // 2
    tree = sum(h - mid for h in height if h > mid)

    if tree >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)