# 입력으로 들어온 문자열 사전에서 찾음
# 사전에 있으면 다음 문자 포함해서 다시 사전에서 찾음
# 사전에 없으면 색인 번호 + 1 해서 사전에 넣기

def solution(msg):
    answer = []
    indices = {}
    cnt = 0
    last = 27
    
    for i in range(26):
        indices[chr(65 + i)] = i + 1
        
    for i in range(len(msg)):
        if cnt > 0:
            cnt -= 1
            continue
        cur_msg = msg[i]
        cur_idx = indices[cur_msg]   # 첫 글자로 색인 초기화
        
        for j in range(i+1, len(msg)):  # 글자 하나씩 추가하며 사전에 있는지 확인
            cur_msg += msg[j]
            
            if cur_msg not in indices:  # 사전에 없는 글자면 추가, 색인 지정, break
                indices[cur_msg] = last
                last += 1
                break
                
            cnt += 1    # 몇 글자 건너 뛸 지 저장
            cur_idx = indices[cur_msg]  # 글자 사전에 있으면 색인 업데이트
        
        answer.append(cur_idx)
    print(indices)
    
    return answer