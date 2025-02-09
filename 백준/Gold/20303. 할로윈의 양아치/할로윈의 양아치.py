'''
그래프 탐색 + dp(평범한 배낭)

서로 친구인 아이들의 그룹에서 각각의 그룹에 속해 있는 아이들 수 i, 가지고 있는 사탕의 수 j
라고 할 때, i들의 합이 k를 넘지 않으면서 j의 최댓값을 찾는 문제.

배낭 문제와 똑같음. 배낭 문제는 무게가 w, 가치가 v인 물건들이 있을 때 무게의 합이 k를 넘지 않으면서
v의 최댓값을 찾는 문제.
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    num = 1
    candies = candy[start]
    queue = deque([start])
    visit[start] = 1

    while queue:
        cur = queue.popleft()

        for nxt in graph[cur]:
            if visit[nxt] == 1:
                continue
            candies += candy[nxt]
            num += 1
            queue.append(nxt)
            visit[nxt] = 1

    groups.append((num, candies))

# n: 아이들 수, m: 관계 수, k: 사탕 빼앗을 수 있는 아이들 수
n, m, k = map(int, input().split())
candy = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
groups = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각각의 그룹을 (아이들 수, 소지한 사탕 수) 튜플로 표현
for i in range(1, n+1):
    if visit[i] == 1:
        continue
    bfs(i)
g = len(groups)

# DP 수행
dp = [0 for _ in range(k)]

for p, c in groups:
    for j in range(k-1, p-1, -1):
        dp[j] = max(dp[j], dp[j-p] + c)

print(dp[k-1])