n ,k = map(int,input().split())
nums = [i+1 for i in range(n)]
per = []
i = 0
length = n

a = 0

while True:
    for j in range(k-1):
        if i == len(nums)-1:
            i = 0
        else:
            i += 1


    per.append(str(nums.pop(i)))
    if i > len(nums)-1:
        i = 0

    if len(nums) == 0:
        break
    a += 1


print('<' + ", ".join(per) + '>')