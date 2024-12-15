import sys

t = int(input())

for i in range(t):
    x = int(sys.stdin.readline())

    print(x//25, end= ' ')
    x -= 25*(x//25)
    print(x//10, end= ' ')
    x -= 10*(x//10)
    print(x//5, end= ' ')
    x -= 5*(x//5)
    print(x//1)