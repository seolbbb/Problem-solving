lst = list(map(int,input().split()))

lst.sort()

while lst[-1] >= lst[0] + lst[1]:
    lst[-1] -= 1

print(sum(lst))