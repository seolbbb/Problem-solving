import sys

t = int(sys.stdin.readline())

for i in range(t):
    k = 0
    strings = str(sys.stdin.readline())
    for j in range(50):
        strings = strings.replace('()','')

        if '(' not in strings and ')' not in strings:
            print('YES')
            k = 1
            break

    if k == 0:
        print('NO')