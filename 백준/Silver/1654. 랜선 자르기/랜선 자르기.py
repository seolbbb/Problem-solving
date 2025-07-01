import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]
left = 1
right = max(line)

while left <= right:
    mid = (left+right) // 2
    cnt = sum(map(lambda x: x//mid, line))

    if cnt >= n:
        left = mid+1
    else:
        right = mid-1

print(right)