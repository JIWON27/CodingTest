def solution(n):
    answer = ''
    while True:
        answer += str(n%3)
        if n//3 == 0:
            break
        n = n // 3
    return int(answer,3)