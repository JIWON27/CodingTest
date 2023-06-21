from collections import deque

def solution(s):
    answer = 0
    s = deque(s)
    while len(s) != 0:
        x = s.popleft()
        cnt_x = 1
        cnt_other = 0
        while len(s) != 0:
            if x == s.popleft():
                cnt_x += 1
            else:
                cnt_other += 1
            if cnt_x == cnt_other:
                break
        answer += 1
    return answer