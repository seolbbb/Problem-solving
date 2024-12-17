import sys
input = sys.stdin.readline

n = int(input())
dic = {}
temp = 0
lst = []
for i in range(n):
    x = int(input())
    lst.append(x)
    if n == 1:
        temp = x
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

if n == 1:
    average = temp
    median = temp
    mode = temp
    diff = 0
else:
    lst.sort()
    a = max(dic.values())
    lst2 = [k for k,v in dic.items() if v == a]
    lst2.sort()
    average = round(sum(lst)/len(lst))
    median = lst[len(lst)//2]
    if len(lst2) == 1:
        mode = lst2[0]
    else:
        mode = lst2[1]
    diff = max(lst)-min(lst)

print(average)
print(median)
print(mode)
print(diff)