import sys

n, m = map(int,sys.stdin.readline().split())
dn = [1,0,-1,0]
dm = [0,1,0,-1]
board = []
visit = [[0 for _ in range(m)] for _ in range(n)]
queue = [0 for _ in range(n*m)]
pictures = []



for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visit[i][j] == 0:
            cnt = 1
            front = 0
            rear = 0
            queue[rear] = [i,j]
            visit[i][j] = 1
            rear += 1
            while front != rear:
                x = queue[front][0]
                y = queue[front][1]
                front += 1
                for k in range(4):
                    nn = x + dn[k]
                    mm = y + dm[k]
                    if nn < 0 or nn >= n or mm < 0 or mm >= m:
                        continue
                    if visit[nn][mm] == 1 or board[nn][mm] == 0:
                        continue
                    visit[nn][mm] = 1
                    cnt += 1
                    queue[rear] = [nn,mm]
                    rear += 1
            pictures.append(cnt)
        
if len(pictures) == 0:
    print(0)
    print(0)
else:
    print(len(pictures))
    print(max(pictures))