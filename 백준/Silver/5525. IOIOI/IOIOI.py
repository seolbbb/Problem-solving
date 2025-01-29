import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()
queue = deque()
p_len = n*2 + 1
ans = 0
cnt = 0

if s[0] == 'I':
    prev = 'O'
else:
    prev = 'I'

for c in s:
    if c == prev:
        queue = deque()
        if c == 'O':
            continue
        else:
            queue.append('I')
            prev = 'I'
    else:
        if len(queue) == p_len:
            queue.popleft()
            queue.append(c)
        else:
            queue.append(c)
        prev = c
    
    if len(queue) == p_len and queue[0] == 'I' and queue[-1] == 'I':
        ans += 1

print(ans)