#킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개

W = [1, 1, 2, 2, 2, 8]
X = list(map(int, input().split()))
Y = []

for i in range(len(W)):
    Y.append(W[i] - X[i])

print(*Y)