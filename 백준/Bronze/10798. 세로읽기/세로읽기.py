strings = ''
X = []

for i in range(5):
    X.append(input())

for i in range(15):
    for j in range(5):
        try:
            strings = strings + X[j][i]
        except IndexError:
            pass
print(strings)