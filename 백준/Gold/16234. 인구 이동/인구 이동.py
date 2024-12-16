from collections import deque
import math

n,l,r = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
queue = deque()
dx = [0,1,0,-1]
dy = [1,0,-1,0]
day = 0

while True:
    union_lst = []
    visit = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                lst = [[i,j]]
                queue.append((i,j))
                visit[i][j] = 1         
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if abs(a[nx][ny] - a[x][y]) < l or abs(a[nx][ny] - a[x][y]) > r:
                            continue
                        if visit[nx][ny] == 1:
                            continue
                        queue.append((nx,ny))
                        visit[nx][ny] = 1
                        lst.append([nx,ny])
                if len(lst) >= 2:
                    union_lst.append(lst)
                    
    if len(union_lst) == 0:
        print(day)
        break
    else:
        for union in union_lst:
            total = 0
            for x,y in union:
                    total += a[x][y]
            popul = math.trunc(total/len(union))
            for x,y in union:
                a[x][y] = popul
        day += 1