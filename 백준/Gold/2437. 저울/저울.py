import sys
input = sys.stdin.readline

n = int(input())
weights = sorted(list(map(int, input().split())))
max_weight = 0

for weight in weights:
    if weight > max_weight+1:
        break
    max_weight += weight

print(max_weight+1)