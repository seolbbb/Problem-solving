import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dist = [[-1 for _ in range(m)] for _ in range(n)]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            queue.append((i, j))
            dist[i][j] = 0
        elif board[i][j] == 0:
            dist[i][j] = 0

while queue:
    x, y = queue.popleft()

    for dx, dy in dir:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == 0 or dist[nx][ny] >= 0:
            continue
        queue.append((nx, ny))
        dist[nx][ny] = dist[x][y] + 1

for row in dist:
    print(*row)