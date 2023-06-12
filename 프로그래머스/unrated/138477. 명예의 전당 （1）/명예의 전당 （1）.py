from collections import deque
def solution(k, score):
    answer = deque()
    result = []
    for i in score:
        if len(answer) == k:
            if answer[0] < i:
                answer.append(i)
                answer.popleft()
        else:
            answer.appendleft(i)
        answer = sorted(answer, key=lambda x:x)
        answer = deque(answer)
        result.append(answer[0])
    return result