def dfs(x, y):
    global r, c, ans
    move = 0

    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= r or ny <0 or ny >= c:
            continue
        if used[ord(board[nx][ny])-65] == 1:
            continue
        move = 1
        used[ord(board[nx][ny])-65] = 1
        dfs(nx,ny)
        used[ord(board[nx][ny])-65] = 0
    
    if move == 0:
        cnt = 0
        for n in used:
            if n == 1:
                cnt += 1
        ans = max(ans, cnt)

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
used = [0 for _ in range(26)]
ans = 0

used[ord(board[0][0])-65] = 1
dfs(0, 0)
print(ans)