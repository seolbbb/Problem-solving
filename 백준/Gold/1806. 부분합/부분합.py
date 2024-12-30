import sys
input = sys.stdin.readline

n,s = map(int,input().split())
seq = list(map(int,input().split()))
head = 0
tail = 0
partial = seq[0]
length = 100001
cnt = 1

while True:
    while partial < s and head < n-1:
        head += 1
        partial += seq[head]
        cnt += 1
    while partial >= s:
        length = min(length,cnt)
        if head > tail:
            partial -= seq[tail]
            tail += 1
            cnt -= 1
        else:
            break
    if head == n-1 or length == 1:
        break

if length == 100001:
    print(0)
else:
    print(length)