import sys
import heapq
input = sys.stdin.readline

n = int(input())

leftHeap = []
rightHeap = []

for i in range(n):
    num = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        left = heapq.heappop(leftHeap)
        right = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -right)
        heapq.heappush(rightHeap, -left)

    print(-leftHeap[0])