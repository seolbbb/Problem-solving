N = input().rstrip()

ans = []
length = 0

for i in range(1, len(N) + 1):
    length = length * 2 + 1

def dfs(left, right, string):
    if len(string) == length:
        ans.append(string)
    if left > 0:
        dfs(left - 1, right, string + N[left - 1] + string)
    if right < len(N) - 1:
        dfs(left, right + 1, string + string + N[right + 1])
        
for i in range(len(N)):
    dfs(i, i, N[i])
print((len(set(ans))))