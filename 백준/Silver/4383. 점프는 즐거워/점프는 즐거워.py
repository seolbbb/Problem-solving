import sys

while True:
    try:
        lst = list(map(int,sys.stdin.readline().split()))
        if lst[0] == 1:
            print('Jolly')
            continue
        s = [i for i in range(1,lst[0])]
        b = []
        for i in range(1,lst[0]):
            b.append(abs(lst[i]-lst[i+1]))
        if sorted(b) == s:
            print('Jolly')
        else:
            print('Not jolly')
    except:
        break