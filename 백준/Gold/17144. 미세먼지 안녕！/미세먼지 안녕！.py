import sys
from collections import deque
input = sys.stdin.readline

def diffusion(row, col, dust):
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if nr < 0 or nr >= r or nc < 0 or nc >= c:
            continue
        if board[nr][nc] == -1:
            continue
        board[nr][nc] += int(dust/5)
        board[row][col] -= int(dust/5)

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]


for _ in range(t):
    dusts = []
    cleaner = []

    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                dusts.append((i, j, board[i][j]))
            elif board[i][j] == -1:
                cleaner.append((i, j))

    for row, col, dust in dusts:
        diffusion(row, col, dust)
    
    r1, c1 = cleaner[0]
    r2, c2 = cleaner[1]
    width1 = r1
    width2 = r2
    c1 += 1
    c2 += 1

    tmp1 = deque([board[r1][c1]])
    tmp2 = deque([board[r2][c2]])
    board[r1][c1] = 0
    board[r2][c2] = 0

    for _ in range(c-2):
        tmp1.append(board[r1][c1+1])
        tmp2.append(board[r2][c2+1])
        board[r1][c1+1] = tmp1.popleft()
        board[r2][c2+1] = tmp2.popleft()
        c1 += 1
        c2 += 1

    for _ in range(r1):
         tmp1.append(board[r1-1][c1])
         board[r1-1][c1] = tmp1.popleft()
         r1 -= 1

    for _ in range(r-(r2+1)):
        tmp2.append(board[r2+1][c2])
        board[r2+1][c2] = tmp2.popleft()
        r2 += 1
    
    for _ in range(c-1):
        tmp1.append(board[r1][c1-1])
        tmp2.append(board[r2][c2-1])
        board[r1][c1-1] = tmp1.popleft()
        board[r2][c2-1] = tmp2.popleft()
        c1 -= 1
        c2 -= 1

    for _ in range(width1-1):
         tmp1.append(board[r1+1][c1])
         board[r1+1][c1] = tmp1.popleft()
         r1 += 1

    for _ in range(r-(width2+2)):
        tmp2.append(board[r2-1][c2])
        board[r2-1][c2] = tmp2.popleft()
        r2 -= 1
    
print(sum([sum(row) for row in board]) + 2)