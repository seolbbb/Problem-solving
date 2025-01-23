def search(r, c, d):
    global ans

    if board[r][c] == 0:
        board[r][c] = 2
        ans += 1
    elif board[r][c] == 1:
        print(ans)
        exit()

    for i in range(4):
        
        new_dir = move[d][i]
        nr = r + new_dir[0]
        nc = c + new_dir[1]

        if board[nr][nc] == 0:
            search(nr, nc, dir[new_dir])
            break

    br = r + dir2[d][0]
    bc = c + dir2[d][1]
    search(br, bc, d)


n, m = map(int,input().split())
r, c, d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

dir = {(-1,0):0,
       (0,1):1,
       (1,0):2,
       (0,-1):3}
dir2 = [(1,0),(0,-1),(-1,0),(0,1)]
move = [[(0,-1),(1,0),(0,1),(-1,0)],
       [(-1,0),(0,-1),(1,0),(0,1)],
       [(0,1),(-1,0),(0,-1),(1,0)],
       [(1,0),(0,1),(-1,0),(0,-1)]]
ans = 0

search(r, c, d)