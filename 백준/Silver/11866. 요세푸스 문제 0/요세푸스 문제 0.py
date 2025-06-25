import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque([i for i in range(1, n+1)])
p = []

while queue:
    queue.rotate(-k+1)
    p.append(queue.popleft())

print('<', end='') 
print(*p, sep=', ', end='')
print('>')