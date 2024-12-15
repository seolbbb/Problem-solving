N = int(input())
X = list(map(int, input().split()))
M = max(X)
sum = 0

for i in range(N):
    sum += (X[i]/M)*100

print(sum/N)