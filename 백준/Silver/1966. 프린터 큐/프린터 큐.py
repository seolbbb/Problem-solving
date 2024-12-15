n = int(input())

for i in range(n):
    m, l = map(int,input().split())
    lst = list(map(int,input().split()))
    numlst = [0 for i in range(m)]
    numlst[l] = 1
    cnt = 0

    while len(lst) > 0:
        if lst[0] >= max(lst):
            cnt += 1
            lst.pop(0)
            numlst.pop(0)
            if 1 not in numlst:
                 break
        else:
            lst.append(lst.pop(0))
            numlst.append(numlst.pop(0))
            if 1 not in numlst:
                break
    print(cnt)