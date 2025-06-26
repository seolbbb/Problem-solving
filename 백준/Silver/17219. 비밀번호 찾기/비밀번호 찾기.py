import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pwd = {}

for _ in range(n):
    site, password = input().rstrip().split()
    pwd[site] = password

for _ in range(m):
    print(pwd[input().rstrip()])