from collections import deque

def move(robots):
    cor = {}
    done = 1    # 전체 이동 완료 여부 flag
    
    for robot in robots:
        r, c = robot[0][0], robot[0][1]
        nr, nc = robot[1][0], robot[1][1]
        if nr == -1:    # 이미 이동 끝낸 경우
            continue
        done = 0
        dr = r - nr # row 방향 거리
        dc = c - nc # column 방향 거리

        if dr != 0: # row 방향 이동 가능하다면
            if dr > 0:  # dr이 0보다 크면 위로 이동
                r -= 1
            else:   # dr이 0보다 작으면 아래로 이동
                r += 1
        elif dc != 0: #column 방향 이동 가능하다면
            if dc > 0:
                c -= 1
            else:
                c += 1

        robot[0][0], robot[0][1] = r, c     # 현재 좌표 갱신        
        if r - nr == 0 and c - nc == 0:  # 다음 좌표에 도착했다면
            nxt = robot[2].popleft()
            robot[1] = [nxt[0], nxt[1]]   # 다음 좌표 갱신
        
        cor[(r, c)] = cor.get((r, c), 0) + 1    # cor(딕셔너리)에 현재 좌표 추가
        
    if done:    # 모두 이동 끝났으면 0 반환, 아니면 현재 좌표들 반환
        return 0
    else:
        return cor
    
def check(cor):
    cnt = 0
    
    if not cor: # cor이 비어 있으면 return -1
        return -1
    
    for count in cor.values():
        if count > 1:
            cnt += 1
    return cnt

def solution(points, routes):
    answer = 0
    cor = {}
    robots = []
    for route in routes:    # robots 초기화, [[현재 좌표], [다음 좌표], [나머지 좌표들]]
        path = [points[i-1] for i in route]
        cur = [path[0][0], path[0][1]]  # 첫 번째 좌표
        nxt = [path[1][0], path[1][1]]  # 그 다음 좌표
        rest = deque([[p[0], p[1]] for p in path[2:]] + [[-1, -1]])   # 나머지 좌표들
        robots.append([cur, nxt, rest])
        
        r, c = points[route[0] - 1][0], points[route[0] - 1][1]
        cor[(r, c)] = cor.get((r, c), 0) + 1
    
    #print("초기", robots)
    answer += check(cor)    # 0초 확인
    
    while True:
        #print("이동 전 :", robots)
        cor = move(robots)
        cnt = check(cor)
        #print("이동 후 :", robots)
        #print(cor)
        #print(cnt)
        if cnt == -1:
            break
        else:
            answer += cnt
    print(answer)
    return answer