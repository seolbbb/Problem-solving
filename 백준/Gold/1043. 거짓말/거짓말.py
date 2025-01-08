def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
true_lst = list(map(int,input().split()))[1:]
parent = [i for i in range(n+1)]
parties = []
cnt = 0

for i in true_lst:
    union(0,i)

for i in range(m):
    party = list(map(int,input().split()))[1:]
    parties.append(party)

    for j in range(len(party)-1):
        union(party[j],party[j+1])

for party in parties:
    if find(party[0]) == 0:
        continue
    cnt += 1

print(cnt)