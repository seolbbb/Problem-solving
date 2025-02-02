from collections import deque
import copy

def air_check():
    global board
    visit = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(m):
            lst = []

            if board[i][j] == 1 or board2[i][j] >= 1:
                continue

            queue.append((i, j))
            visit[i][j] = 0
            covered = 1

            while queue:
                x, y = queue.popleft()
                for p in range(4):
                    nx = x + dx[p]
                    ny = y + dy[p]
                    # board 밖으로 나갈 수 있다면 치즈로 둘러쌓이지 않은 것
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        covered = 0
                        continue
                    if board[nx][ny] >= 1 or visit[nx][ny] == 1:
                        continue
                    queue.append((nx, ny))
                    lst.append((nx, ny))
                    visit[nx][ny] = 1
                    
            # 바깥 공기: 2, 둘러쌓인 공기: 3
            if covered == 1:
                for x, y in lst:
                    board2[x][y] = 3
            else:
                for x, y in lst:
                    board2[x][y] = 2

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
time = 0
cheese = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            cheese.append((i, j))
            
board2 = copy.deepcopy(board)
air_check()

while cheese:
    s1 = set(cheese)
    rot = []
    time += 1

    for x, y in cheese:
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바깥 공기와 맞닿은 면이 2개 이상이면 rot에 추가.
            if board2[nx][ny] == 2:
                cnt += 1
        if cnt >= 2:
            rot.append((x, y))

    for x, y in rot:
        board[x][y] = 0

    s2 = set(rot)
    cheese = list(s1 - s2)
    board2 = copy.deepcopy(board)
    air_check()

print(time)