import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque(enumerate(map(int, input().split())))
ans = []

while queue:
    idx, move = queue.popleft()
    ans.append(idx + 1)

    if move > 0:
        queue.rotate(-(move - 1))
    elif move < 0:
        queue.rotate(-move)

print(' '.join(map(str, ans)))