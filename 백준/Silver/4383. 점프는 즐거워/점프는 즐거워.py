import sys

while True:
    try:
        lst = list(map(int,sys.stdin.readline().split()))
        s = [i for i in range(1,lst[0])]
        o = 0
        for i in range(1,lst[0]):
            if abs(lst[i]-lst[i+1]) in s:
                s.remove(abs(lst[i]-lst[i+1]))
                pass
            else:
                print('Not jolly')
                o = 1
                break
        if o == 0:
            print('Jolly')
    except:
        break