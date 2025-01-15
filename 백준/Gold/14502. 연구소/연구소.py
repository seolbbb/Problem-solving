from collections import deque
import copy

n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
wall_cnt = 0
virus = []
empty = []
area = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append((i,j))
        if board[i][j] == 1:
            wall_cnt += 1
        if board[i][j] == 0:
            empty.append((i,j))

for i in range(len(empty) - 2):
    for j in range(i + 1,len(empty) - 1):
        for k in range(j + 1,len(empty)):
            board2 = copy.deepcopy(board)
            a, b = empty[i]
            board2[a][b] = 1
            a, b = empty[j]
            board2[a][b] = 1
            a, b = empty[k]
            board2[a][b] = 1

            queue = deque()
            cnt = 0

            for vx, vy in virus:
                queue.append((vx,vy))
                board2[vx][vy] = 2

                while queue:
                    x, y = queue.popleft()
                    for t in range(4):
                        nx = x + dx[t]
                        ny = y + dy[t]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if board2[nx][ny] == 1 or board2[nx][ny] == 2:
                            continue
                        queue.append((nx,ny))
                        board2[nx][ny] = 2
            
            for q in range(n):
                for w in range(m):
                    if board2[q][w] == 0:
                        cnt += 1

            area.append(cnt)

print(max(area))