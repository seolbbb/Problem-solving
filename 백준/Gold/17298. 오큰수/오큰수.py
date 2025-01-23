import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
ans = [-1 for _ in range(n)]
hq = []

for i in range(n):
    heapq.heappush(hq, (arr[i],i))

    while hq and hq[0][0] < arr[i]:
        num, idx = heapq.heappop(hq)
        ans[idx] = arr[i]

print(' '.join(map(str, ans)))