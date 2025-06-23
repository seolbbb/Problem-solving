import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    a, b = map(str, input().rstrip().split())
    a = int(a)
    lst.append((a, b))

lst.sort(key = lambda x:x[0])

for age, name in lst:
    print(age, name)