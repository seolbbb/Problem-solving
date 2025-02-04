import sys
sys.setrecursionlimit(10**7)

def backtrack(num, coord):
    global tmp, cnt

    if len(coord) - num + cnt < tmp:
        return

    tmp = max(tmp, cnt)
    
    for i in range(num, len(coord)):
        x, y = coord[i]
        if diag1[x+y] == 1 or diag2[n-(x-y+1)] == 1:
            continue
        diag1[x+y] = 1
        diag2[n-(x-y+1)] = 1
        cnt += 1
        backtrack(i+1,coord)
        diag1[x+y] = 0
        diag2[n-(x-y+1)] = 0
        cnt -= 1

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
diag1 = [1 for _ in range(2*n-1)]
diag2 = [1 for _ in range(2*n-1)]
coord1 = []
coord2 = []
cnt = 0
tmp = 0
black = 0
white = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            if (i+j)%2 == 0:
                coord1.append((i, j))
            else:
                coord2.append((i, j))
            diag1[i+j] = 0
            diag2[n-(i-j+1)] = 0

backtrack(0, coord1)
black = tmp
tmp = 0
backtrack(0, coord2)
white = tmp
print(black + white)