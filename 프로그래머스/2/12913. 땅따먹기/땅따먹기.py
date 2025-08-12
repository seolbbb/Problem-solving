def solution(land):
    answer = 0
    dp = [[0 for _ in range(5)] for _ in range(len(land)+1)]
    
    for i in range(1, len(land) + 1):
        for j in range(1, 5):
            dp[i][j] = max([dp[i-1][k] for k in range(1, 5) if k != j]) + land[i-1][j-1]
    
    answer = max(dp[len(land)])

    return answer