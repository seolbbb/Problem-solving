import sys
input = sys.stdin.readline

def backtrack(start):
    if len(team1) == n//2:
        team2 = [i for i in range(1,n+1) if i not in team1]
        team1_score = 0
        team2_score = 0

        for i in range(len(team1)):
            for j in range(i+1,len(team1)):
                a, b = team1[i], team1[j]
                team1_score += s[a-1][b-1] + s[b-1][a-1]
        for i in range(len(team2)):
            for j in range(i+1,len(team2)):
                a, b = team2[i], team2[j]
                team2_score += s[a-1][b-1] + s[b-1][a-1]
        
        results.append(abs(team2_score - team1_score))
        return

    for i in range(start,n+1):
        team1.append(i)
        backtrack(i + 1)
        team1.pop()

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
team1 = []
results = []

backtrack(1)

print(min(results))