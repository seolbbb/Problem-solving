n, m = map(int,input().split())
lst = []
cnt1 = 0
cnt2 = 0
values = []

for i in range(n):
    lst.append(input())

for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for k in range(8):
            for l in range(8):
                if (k+l)%2 == 0:
                    if lst[i+k][j+l] != 'B':
                        cnt1 +=1
                    if lst[i+k][j+l] != 'W':
                        cnt2 +=1
                else:
                    if lst[i+k][j+l] != 'W':
                        cnt1 += 1
                    if lst[i+k][j+l] != 'B':
                        cnt2 += 1
        values.append(cnt1)
        values.append(cnt2)

print(min(values))