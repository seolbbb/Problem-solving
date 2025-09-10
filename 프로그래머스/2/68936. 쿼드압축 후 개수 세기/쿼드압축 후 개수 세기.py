cnt_zero = 0
cnt_one = 0

def solution(arr):

    
    def quad(r, c, size):
        global cnt_zero
        global cnt_one
        cur = arr[r][c]
        
        for i in range(r, r + size):
            for j in range(c, c + size):
                if arr[i][j] != cur:
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