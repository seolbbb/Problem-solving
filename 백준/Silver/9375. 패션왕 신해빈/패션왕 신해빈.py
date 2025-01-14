import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    cat = defaultdict(int)
    cnt = 1

    for _ in range(n):
        i, c = input().rstrip().split()
        cat[c] += 1
    
    for val in cat.values():
        cnt *= val + 1

    print(cnt-1)