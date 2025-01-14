import sys
from collections import deque
input = sys.stdin.readline

def D(n):
   return (2*n) % 10000

def S(n):
    return (n -1) if n != 0 else 9999

def L(n):
    return (n % 1000) * 10 + n // 1000

def R(n):
    return (n % 10) * 1000 + n // 10

t = int(input())

for _ in range(t):
    a, b = map(int,input().split())

    queue = deque()
    visited = [0 for _ in range(10000)]
    prev = [-1 for _ in range(10000)]
    cur_cmd = ['' for _ in range(10000)]

    queue.append(a)
    visited[a] = 1

    while queue:
        x = queue.popleft()
        
        if x == b:
            break
        
        for cmd in ['D','S','L','R']:
            if cmd == 'D':
                nx = D(x)
            elif cmd == 'S':
                nx = S(x)
            elif cmd == 'L':
                nx = L(x)
            elif cmd == 'R':
                nx = R(x)

            if visited[nx] > 0:
                continue
            queue.append(nx)
            visited[nx] = 1
            cur_cmd[nx] = cmd
            prev[nx] = x

    ans = []
    cur = b
    while cur != a:
        ans.append(cur_cmd[cur])
        cur = prev[cur]

    ans.reverse()
    print(''.join(ans))