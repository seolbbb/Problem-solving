S = list(input().upper())
SS = list(set(S))
cnt = []

for i in SS:
    count = S.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(SS[cnt.index(max(cnt))])