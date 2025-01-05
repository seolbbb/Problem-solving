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

def star2(num):
    if num == 1:
        return ['*']
    
    stars = star2(num//3)
    l = []

    for s in stars:
        l.append(s*3)
    for s in stars:
        l.append(s + ' ' * (num//3) + s)
    for s in stars:
        l.append(s*3)
    return l

n = int(input())
arr = [[' ' for _ in range(n)] for _ in range(n)]

print('\n'.join(star2(n)))

# star(0,0,n)
# for i in range(n):
#     print(''.join(arr[i]))