from collections import deque
def solution(ingredient):
    answer = []
    cnt = 0
    q = deque(ingredient)
    while len(q) > 0:
        answer.append(q.popleft())
        if len(answer) >= 4 :
            if answer[-4] == 1 and answer[-3] == 2 and answer[-2] == 3 and answer[-1] == 1:
                for _ in range(4):
                    answer.pop()
                #answer = answer[:len(answer)-4] # 여기를 줄여야할꺼같음..시간..
                cnt += 1
    return cnt