import sys

n = int(sys.stdin.readline())
total = 0
middle = 0
lst = [0 for _ in range(n)]
lst2 = []
cnt = {}

if n == 1:
    x = int(sys.stdin.readline())
    print(x)
    print(x)
    print(x)
    print(0)

else:
    for i in range(n):
        x = int(sys.stdin.readline())
        lst[i] = x
    
    uniq = set(lst)
    print(round(sum(lst)/n))
    print(sorted(lst)[n//2])

    # for num in uniq:
    #     lst2.append([num, lst.count(num)])
    # 위 list.count()는 시간복잡도가 O(n)임. 
    # 그래서 전체 시간복잡도가 O(n^2)가 되서 시간초과가 나는듯.
    # lst2.sort(key= lambda x: x[1], reverse= True)
    # cnt = max([x[1] for x in lst2])
    # lst3 = [x[0] for x in lst2 if x[1] == cnt]

    # if len(lst3) == 1:
    #     print(lst3[0])
    # else:
    #     print(sorted(lst3)[1])

    for i in range(n):
        if lst[i] not in cnt:
            cnt[lst[i]] = 1
        else:
            cnt[lst[i]] += 1
    
    lst3 = []

    for key, value in cnt.items():
        if value == max(cnt.values()):
            lst3.append(key)
    
    if(len(lst3)) == 1:
        print(lst3[0])
    else:
        print(sorted(lst3)[1])

    print(max(lst)-min(lst))