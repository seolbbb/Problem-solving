import sys

while True:
    lst = list(map(int,sys.stdin.readline().split()))
    if 0 in lst:
        break    
    lst.sort()

    if lst[-1] >= lst[0] + lst[1]:
        print('Invalid')
    else:
        if lst.count(lst[0]) == 3:
            print('Equilateral')
        elif lst[0] == lst[1] or lst[1] == lst[2] or lst[2] == lst[0]:
            print('Isosceles')
        else:
            print('Scalene')