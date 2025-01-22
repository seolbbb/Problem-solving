import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# def bfs(row, col, n_arr):
#     dist = [[-1 for _ in range(n)] for _ in range(n)]
#     queue = deque()
#     queue.append((row,col))
#     dist[row][col] = 0

#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if dist[nx][ny] >= 0:
#                 continue
#             if n_arr[nx][ny] == 2:
#                 return dist[x][y] + 1
            
#             queue.append((nx,ny))
#             dist[nx][ny] = dist[x][y] + 1
    
# chicken 13 C 6 = 1716, bfs 2500 * 100

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
chicken = []
home = []
ans = float('inf')

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i,j))
        elif arr[i][j] == 2:
            chicken.append((i,j))

cases = list(combinations(chicken,m))

for i in range(len(cases)):
    dist = 0

    for r1, c1 in home:
        temp = 251
        for r2, c2 in cases[i]:
            temp = min(temp, abs(r1-r2) + abs(c1-c2))
        dist += temp
    ans = min(ans, dist)

print(ans)