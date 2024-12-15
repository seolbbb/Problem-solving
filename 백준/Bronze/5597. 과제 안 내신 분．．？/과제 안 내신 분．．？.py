a = []
for i in range(30):
    a.append(i+1)

while len(a) > 2:
    a.remove(int(input()))
a.sort()
print(a[0])
print(a[1])