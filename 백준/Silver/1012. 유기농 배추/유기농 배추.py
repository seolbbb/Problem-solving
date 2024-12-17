import sys
from collections import deque

t = int(sys.stdin.readline())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    cab = [[0 for _ in range(m)] for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    cnt = 0

    for i in range(k):
        x, y = map(int,sys.stdin.readline().split())
        cab[y][x] = 1

    for i in range(n):
        for j in range(m):
            if cab[i][j] == 1 and visit[i][j] == 0:
                queue.append((i,j))
                visit[i][j] = 1
                cnt += 1

                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if cab[nx][ny] == 0 or visit[nx][ny]:
                            continue
                        queue.append((nx,ny))
                        visit[nx][ny] = 1
    print(cnt)