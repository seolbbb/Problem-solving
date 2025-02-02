from collections import deque
n = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]

board = [list(map(int, input().split())) for _ in range(n)]
t = 0
eat = 0
size = 2

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            start = (i, j)

while True:
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    fishes = []
    queue = deque()
    sx, sy = start
    queue.append(start)
    dist[sx][sy] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] > size or dist[nx][ny] >= 0:
                continue
            queue.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1
            if 0 < board[nx][ny] < size:
                fishes.append((dist[nx][ny], nx, ny))

    if len(fishes) == 0:
        break
    fishes = sorted(fishes, key=lambda x: (x[0],x[1],x[2]))
    move, fx, fy = fishes[0]
    start = (fx, fy)
    board[fx][fy] = 0
    t += move
    eat += 1
    if eat == size:
        eat = 0
        size += 1

print(t)