import sys

n, m = map(int,sys.stdin.readline().split())
password = {}


for i in range(n):
    a, b = map(str,sys.stdin.readline().rstrip().split())

    password[a] = b

for i in range(m):
    print(password[sys.stdin.readline().rstrip()])