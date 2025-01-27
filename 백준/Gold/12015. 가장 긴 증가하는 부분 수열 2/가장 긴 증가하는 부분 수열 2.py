import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
lis = [0]

for num in arr:
    if num > lis[-1]:
        lis.append(num)
    else:
        idx = bisect_left(lis, num)
        lis[idx] = num

print(len(lis)-1)