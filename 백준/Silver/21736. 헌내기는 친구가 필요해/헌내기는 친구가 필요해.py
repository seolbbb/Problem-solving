import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
board = [list(input().rstrip()) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
queue = deque([])
ans = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            queue.append((i, j))
            visit[i][j] = 1

while queue:
    x, y = queue.popleft()

    for dx, dy in dir:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visit[nx][ny] == 1 or board[nx][ny] == 'X':
            continue
        if board[nx][ny] == 'P':
            ans += 1
        
        queue.append((nx, ny))
        visit[nx][ny] = 1

print(ans if ans else 'TT')