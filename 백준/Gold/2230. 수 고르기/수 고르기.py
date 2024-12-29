import sys
input = sys.stdin.readline

n,m = map(int,input().split())
seq = [int(input()) for _ in range(n)]
seq.sort()
front = 0
diff = 2000000000

for end in range(1,n):
    if abs(seq[end] - seq[front]) < m:
        continue
    while abs(seq[end] - seq[front]) >= m:
        diff = min(abs(seq[end] - seq[front]),diff)
        if diff == m:
            print(diff)
            exit(0)
        if end - front == 1:
            break
        front += 1

print(diff)