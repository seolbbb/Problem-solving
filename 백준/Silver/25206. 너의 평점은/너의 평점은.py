score = {'A+':4.5, 'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,
         'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
X = []
sum = 0
denom = 0

for i in range(20):
    X.append(list(input().split()))

for i in range(20):
    if X[i][2] == 'P':
        pass
    else:
        sum += (float((X[i][1])) * score[X[i][2]])
        denom += float((X[i][1]))

print(sum/denom)