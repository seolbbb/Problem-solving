from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
dist = [[-1 for _ in range(m)] for _ in range(n)]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

queue = deque([(0, 0)])
dist[0][0] = 1

while queue:
    x, y = queue.popleft()

    for dx, dy in dir:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] >= 0 or board[nx][ny] == 0:
            continue
        queue.append((nx, ny))
        dist[nx][ny] = dist[x][y] + 1

print(dist[-1][-1])