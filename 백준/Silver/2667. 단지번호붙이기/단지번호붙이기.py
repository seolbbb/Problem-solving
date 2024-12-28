import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
apt = [[] for _ in range(n)]
apt_num = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
queue = deque()
visit = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    apt[i] = list(map(int,input().rstrip()))

for i in range(n):
    for j in range(n):
        cnt = 0
        if visit[i][j] == 1 or apt[i][j] == 0:
            continue
        queue.append((i,j))
        visit[i][j] = 1

        while queue:
            cnt += 1
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if visit[nx][ny] == 1 or apt[nx][ny] == 0:
                    continue
                queue.append((nx,ny))
                visit[nx][ny] = 1
        apt_num.append(cnt)

apt_num.sort()

print(len(apt_num))
for num in apt_num:
    print(num)