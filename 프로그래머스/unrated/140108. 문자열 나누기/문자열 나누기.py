from collections import deque
def solution(string):
    answer = 0
    s = deque(string)
    while len(s) != 0:
        x = s.popleft()
        if len(s) == 0: # 뒤에 더 이상 읽을 문자가 없는 경우
            return answer + 1
        cnt_x = 1
        cnt_other = 0
        for other in s:
            if x == other:
                cnt_x += 1
            else:
                cnt_other += 1
            if cnt_x == cnt_other:
                for _ in range(cnt_x*2-1):
                    s.popleft()
                answer += 1
                break
        if cnt_x != cnt_other:
            answer += 1
            for _ in range(cnt_x + cnt_other - 1):
                s.popleft()
    return answer