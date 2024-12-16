from collections import deque
import sys

r, c = map(int,sys.stdin.readline().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
maze = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
time = [[-1 for _ in range(c)] for _ in range(r)]
time2 = [[-1 for _ in range(c)] for _ in range(r)]
player = deque()
fire = deque()

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            player.append((i,j))
            time[i][j] = 0
        elif maze[i][j] == 'F':
            fire.append((i,j))
            time2[i][j] = 0

while fire:  
    x, y = fire.popleft()
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= r or yy < 0 or yy >= c:
            continue
        if maze[xx][yy] == '#' or time2[xx][yy] >= 0:
            continue
        fire.append((xx,yy))
        time2[xx][yy] = time2[x][y] + 1

while player:
    x, y = player.popleft()
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= r or yy < 0 or yy >= c:
            print(time[x][y] + 1)
            exit(0)
        if maze[xx][yy] != '.' or time[xx][yy] >= 0:
            continue
        if time2[xx][yy] != -1 and time2[xx][yy] <= time[x][y] + 1:
            continue
        player.append((xx,yy))
        time[xx][yy] = time[x][y] + 1

print('IMPOSSIBLE')