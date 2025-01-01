import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    com = input().rstrip()
    n = int(input())
    try:
        arr = deque(map(int,input().strip('[]\n').split(',')))
    except:
        arr = deque()
    flip = 0
    err = 0
    cnt = 0

    for func in com:
        if func == 'R':
            cnt += 1
            if flip == 0:
                flip = 1
            else:
                flip = 0
        elif func == 'D' and len(arr) > 0:
            if flip == 0:
                arr.popleft()
            else:
                arr.pop()
        else:
            err = 1
            break

    if cnt % 2 == 1:
        arr = list(arr)[::-1]

    if err == 1:
        print('error')
    else:
        lst = [str(c) for c in arr]
        print('[' + ','.join(lst) + ']')