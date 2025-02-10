n = input()
ans = -1

if '0' not in n:
    print(-1)
    exit()

total = 0
for c in n:
    total += int(c)
    
if total % 3 != 0:
    print(-1)
    exit()

sorted_num = sorted(n, reverse= True)
print(''.join(sorted_num))