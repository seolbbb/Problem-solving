n = int(input())

cnt = 0

for i in range(n):
    m = 0
    s = input()
    s2 = set(s)
    for j in s2:
        if s.count(j) <= 1:
            pass
        else:
            while True:
                t1 = s.find(j)
                s = s.replace(j,'*',1)
                t2 = s.find(j)
                if t2 == -1:
                    break
                elif t2 - t1 > 1:
                    m = 1
                    break
    if m == 0:
        cnt += 1
    else:
        pass

print(cnt)