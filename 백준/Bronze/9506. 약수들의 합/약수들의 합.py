import sys
divisor = []

while True:
    n = int(sys.stdin.readline())
    divisor = [i for i in range(1,n+1) if n % i == 0]
    if n == -1:
        break
    if sum(divisor[:-1]) == n:
        print('%d = ' %n, end = '')
        print(' + '.join(map(str,divisor[:-1])))
    else:
        print('%d is NOT perfect.' %n)