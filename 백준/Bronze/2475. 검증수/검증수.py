S = list(map(int,input().split()))
Sum = 0

for i in S:
    Sum += (i * i)

print(Sum % 10)
