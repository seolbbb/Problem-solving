cnt_zero = 0
cnt_one = 0

def solution(arr):
    def quad(r, c, size):
        global cnt_zero
        global cnt_one
        cur = arr[r][c]     # 처음 값 기록
        
        for i in range(r, r + size):    
            for j in range(c, c + size):
                if arr[i][j] != cur:    # 구역 탐색하다가 처음 값과 다른 값 있으면, 다시 4등분으로 나누어서 재귀
                    for k in range(2):
                        for l in range(2):
                            quad(r + k * (size//2), c + l * (size//2), size//2)
                    return
        if cur == 0:
            cnt_zero += 1
        else:
            cnt_one += 1
    
    quad(0, 0, len(arr))
    answer = [cnt_zero, cnt_one]
        
    return answer