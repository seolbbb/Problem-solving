def backtrack(r, c):
    global ans

    if sum(tetro) + (4 - len(tetro)) * max_val <= ans:
        return

    if len(tetro) == 4:
        ans = max(ans, sum(tetro))
        return
    
    for move in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx = r + move[0]
        ny = c + move[1]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visit[nx][ny] == 1:
            continue
        visit[nx][ny] = 1
        tetro.append(board[nx][ny])
        backtrack(nx, ny)
        visit[nx][ny] = 0
        tetro.pop()

def backtrack2(r, c):
    global ans

    if sum(tetro) + (4 - len(tetro)) * max_val <= ans:
        return

    if len(tetro) == 4:
        ans = max(ans, sum(tetro))
        return

    for move in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx = r + move[0]
        ny = c + move[1]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visit[nx][ny] == 1:
            continue
        visit[nx][ny] = 1
        tetro.append(board[nx][ny])
        backtrack2(r, c)
        visit[nx][ny] = 0
        tetro.pop()

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
tetro = []
max_val = 0
ans = 0

for row in board:
    max_val = max(max_val, max(row))

for i in range(n):
    for j in range(m):
        tetro.append(board[i][j])
        visit[i][j] = 1
        backtrack(i, j)
        backtrack2(i, j)
        tetro.pop()
        visit[i][j] = 0

print(ans)