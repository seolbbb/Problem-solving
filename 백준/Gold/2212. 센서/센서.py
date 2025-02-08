import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
lst = list(map(int, input().split()))

if k >= n:
    print(0)
    exit()

lst.sort()

gaps = []
for i in range(1, n):
    gaps.append(lst[i] - lst[i-1])

gaps.sort(reverse=True)
min_dist = sum(gaps[k-1:])

print(min_dist)