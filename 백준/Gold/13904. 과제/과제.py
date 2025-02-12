import heapq
n = int(input())
hw = []
hq = []
cnt = 0

for _ in range(n):
    d, w = map(int, input().split())
    hw.append((d, w))
hw.sort()


for i in range(n):
    d, w = hw[i]
    heapq.heappush(hq, w)

    if d <= i-cnt:
        heapq.heappop(hq)
        cnt += 1
    prev = d

print(sum(hq))