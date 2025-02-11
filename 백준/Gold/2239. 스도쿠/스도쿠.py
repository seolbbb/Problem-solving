import sys
sys. setrecursionlimit(10**7)
input = sys.stdin.readline

def sudoku(num):
    if num == len(empty):
        for line in board:
            print(''.join(map(str, line)))
        exit()

    r, c = empty[num]

    for i in range(1, 10):
        if row[r][i] == 1 or col[c][i] == 1 or square[r//3][c//3][i] == 1:
            continue
        row[r][i] = 1
        col[c][i] = 1
        square[r//3][c//3][i] = 1
        board[r][c] = i
        sudoku(num+1)
        row[r][i] = 0
        col[c][i] = 0
        square[r//3][c//3][i] = 0
        board[r][c] = 0
    
board = [list(map(int, list(input().rstrip()))) for _ in range(9)]
row = [[0 for _ in range(10)] for _ in range(9)]
col = [[0 for _ in range(10)] for _ in range(9)]
square = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(3)]
empty = []

for i in range(9):
    for j in range(9):
        row_num = board[i][j]
        col_num = board[j][i]
        # 각 행, 각 네모칸에서 1~9 중 가지고 있는 숫자 체크
        if row_num != 0:
            row[i][row_num] = 1
            square[i//3][j//3][row_num] = 1
        # 빈자리 체크
        else:
            empty.append((i, j))
        # 각 열에서 1~9 중 가지고 있는 숫자 체크
        if col_num != 0:
            col[i][col_num] = 1
        
sudoku(0)

# print(empty)
# print(*row, sep= '\n')
# print()
# print(*col, sep= '\n')
# print()
# print(*square, sep= '\n')