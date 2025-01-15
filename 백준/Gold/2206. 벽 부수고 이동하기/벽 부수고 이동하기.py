import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    dist = [[[-1,-1] for _ in range(m)] for _ in range(n)]

    queue.append((0,0,0))
    dist[0][0][0] = 1

    while queue:
        x, y, used = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 0 and dist[nx][ny][used] == -1:
                dist[nx][ny][used] = dist[x][y][used] + 1
                queue.append((nx,ny,used))
            elif board[nx][ny] == 1 and used == 0:
                dist[nx][ny][1] = dist[x][y][used] + 1
                queue.append((nx,ny,1))

    if dist[n-1][m-1][0] == -1:
        return dist[n-1][m-1][1] 
    if dist[n-1][m-1][1] == -1:
        return dist[n-1][m-1][0]
    
    return min(dist[n-1][m-1][0], dist[n-1][m-1][1])

n, m = map(int,input().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
board = [list(map(int,list(input().rstrip()))) for _ in range(n)]

res = bfs()
print(res)