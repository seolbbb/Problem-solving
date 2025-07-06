import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
idx = {}
i = 0

for k in sorted(set(lst)):
    idx[k] = i
    i += 1

print(*[idx[m] for m in lst])