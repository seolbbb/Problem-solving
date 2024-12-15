Char = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
X = input()
n = len(X)
time = 0

for i in range(n):
    time += 2
    for j in range(len(Char)):
        if X[i] in Char[j]:
            time += j + 1
    
print(time)