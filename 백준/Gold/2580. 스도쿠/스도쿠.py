def sudoku(start):
    if start == len(zeros):
        for i in range(9):
            print(' '.join(map(str,board[i])))
        exit(0)
    
    r, c = zeros[start]

    for i in range(1,10):
        if  row[r][i] == 0 and col[c][i] == 0 and square[r//3][c//3][i] == 0:
            board[r][c] = i
            row[r][i] = 1
            col[c][i] = 1
            square[r//3][c//3][i] = 1
            sudoku(start + 1)
            board[r][c] = 0
            row[r][i] = 0
            col[c][i] = 0
            square[r//3][c//3][i] = 0

board = [list(map(int,input().split())) for _ in range(9)]
square = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(3)]
row = [[0 for _ in range(10)] for _ in range(9)]
col = [[0 for _ in range(10)] for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        cur1 = board[i][j]
        cur2 = board[j][i]
        if cur1 != 0:
            row[i][cur1] = 1
        else:
            zeros.append((i,j))
        if cur2 != 0:
            col[i][cur2] = 1

for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                cur = board[3*i+k][3*j+l]
                if cur != 0:
                    square[i][j][cur] = 1

sudoku(0)