# 대기실 전체 순회, 응시자가 앉아있는 자리 기준으로 BFS, 거리가 2 이하인 곳에 다른 응시자 있으면 불가능

from collections import deque

def solution(places):
    answer = []
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for place in places:
        flag = 1
        for i in range(5):
            if flag == 0:
                break
            for j in range(5):
                if flag == 0:
                    break
                if place[i][j] == "P":  # 응시자가 있는 곳에 도달
                    dist = [[-1 for _ in range(5)] for _ in range(5)]    # dist 배열 초기화
                    queue = deque([(i, j)])   # queue에 현재 위치 추가
                    dist[i][j] = 0  # 현재 위치 거리 0으로 설정
                    
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in move:
                            nx = x + dx
                            ny = y + dy
                            
                            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:  # 배열 index 넘어가면 continue
                                continue
                            if dist[nx][ny] >= 0:    # 이미 방문한 곳이면 continue
                                continue
                            if place[nx][ny] == "X":  # 방문한 곳이 파티션이면 continue
                                continue
                            
                            dist[nx][ny] = dist[x][y] + 1   # 현재 방문한 곳 거리 업데이트
                            if dist[nx][ny] > 2:    # 현재 거리가 2 이상이면 continue
                                continue    
                            if place[nx][ny] == "P":  # 방문한 곳에 방문자가 있으면 flag = 0, 루프 탈출
                                flag = 0
                                break
                            queue.append((nx, ny))  # queue에 현재 위치 추가
        answer.append(flag)
                            
    return answer