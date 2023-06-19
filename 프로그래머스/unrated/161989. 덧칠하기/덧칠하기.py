def solution(n, m, section):
    answer = 0
    curr = 0
    for idx in section:
        if idx > curr:
            curr = idx+m-1
            answer += 1
    return answer