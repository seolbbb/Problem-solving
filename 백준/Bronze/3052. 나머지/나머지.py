lst = []

for i in range(10):
    a = int(input())
    lst.append(a%42)

print(len(set(lst)))