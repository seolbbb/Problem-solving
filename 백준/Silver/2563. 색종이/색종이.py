s = [0 for _ in range(10000)]

n = int(input())

for i in range(n):
    x, y = map(int,input().split())

    for j in range(10):
        for k in range(10):
            s[((y+j)*100)+x+k] = 1

print(s.count(1))