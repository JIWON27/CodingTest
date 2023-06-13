def solution(k, m, score):
    answer = 0
    score.sort()
    if len(score) % m == 0:
        score = score[::m]
        answer = sum(score) * m
    else:
        answer = sum(score[-m::-m]) * m
    return answer