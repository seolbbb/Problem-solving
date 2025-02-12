import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
pos = [0 for _ in range(n+1)]
max_lis = 0

for num in line:
    pos[num] = pos[num-1] + 1
    max_lis = max(max_lis, pos[num])

print(n - max_lis)