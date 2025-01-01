import sys
input = sys.stdin.readline

n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)
total = sum(rope)
weight = 0

for i in range(n,0,-1):
    weight = max(weight,rope.pop() * i)

print(weight)