import sys

while True:
    x, y = map(int,sys.stdin.readline().split())

    if x == 0 and y == 0:
        break
    elif y % x == 0:
        print('factor')
    elif x % y == 0:
        print('multiple')
    else:
        print('neither')