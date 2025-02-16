import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])

min_gap = 1
max_gap = house[-1] - house[0]

while max_gap >= min_gap:
    mid_gap = (max_gap + min_gap) // 2
    prev = house[0]
    cnt = 1

    for i in range(1, n):
        if house[i] - prev >= mid_gap:
            prev = house[i]
            cnt += 1
    if cnt >= c:
        min_gap = mid_gap + 1
    else:
        max_gap = mid_gap - 1

print(max_gap)