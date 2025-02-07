import copy

#방향 배열 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(direction, x, y, color, board):

    new_board = copy.deepcopy(board)
    new_board[x][y] = '.'
    fell = False

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if new_board[nx][ny] == '#' or new_board[nx][ny] == 'B' or new_board[nx][ny] == 'R':
            break
        if new_board[nx][ny] == 'O':
            x, y = nx, ny
            fell = True
            break
        x, y = nx, ny

    if not fell:
        new_board[x][y] = color
    return x, y, fell, new_board

def dfs(depth, prev, rx, ry, bx, by, board):
    global ans
    if depth == 11:
        return

    for direction in range(4):
        # 이전 이동의 반대 방향 제한
        if prev != -1 and direction == (prev+2) % 4:
            continue

        # 어떤 구슬을 먼저 이동시킬지 결정
        if direction == 0:
            r_first = (rx <= bx)
        elif direction == 1:
            r_first = (ry >= by)
        elif direction == 2:
            r_first = (rx >= bx)
        elif direction == 3:
            r_first = (ry <= by)

        new_board = copy.deepcopy(board)
        if r_first:
            nrx, nry, red_fell, new_board = move(direction, rx, ry, 'R', new_board)
            nbx, nby, blue_fell, new_board = move(direction, bx, by, 'B', new_board)
        else:
            nbx, nby, blue_fell, new_board = move(direction, bx, by, 'B', new_board)
            nrx, nry, red_fell, new_board = move(direction, rx, ry, 'R', new_board)

        if blue_fell:
            continue

        if red_fell:
            ans = min(ans, depth)
            return

        if rx == nrx and ry == nry and bx == nbx and by == nby:
            continue

        dfs(depth + 1, direction, nrx, nry, nbx, nby, new_board)


n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
ans = 11

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red_x, red_y = i, j
        if board[i][j] == 'B':
            blue_x, blue_y = i, j

dfs(1, -1, red_x, red_y, blue_x, blue_y, board)
print(ans if ans <= 10 else -1)