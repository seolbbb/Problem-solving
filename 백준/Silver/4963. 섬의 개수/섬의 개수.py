import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, 1, -1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]
    visit = [[0 for _ in range(w)] for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):

            if board[i][j] == 0 or visit[i][j] == 1:
                continue

            queue = deque([(i, j)])
            visit[i][j] = 1
            cnt += 1

            while queue:
                x, y = queue.popleft()

                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or nx >= h or ny < 0 or ny >= w:
                        continue
                    if visit[nx][ny] == 1 or board[nx][ny] == 0:
                        continue

                    queue.append((nx, ny))
                    visit[nx][ny] = 1

    print(cnt)