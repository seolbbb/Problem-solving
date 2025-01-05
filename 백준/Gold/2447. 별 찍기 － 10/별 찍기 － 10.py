def star(r,c,num):
    if num == 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                arr[r+i][c+j] = '*'
        return
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            star(r+i*(num//3),c+j*(num//3),num//3)

n = int(input())
arr = [[' ' for _ in range(n)] for _ in range(n)]
star(0,0,n)

for i in range(n):
    print(''.join(arr[i]))