def solution(n):
    cnt = 1
    for i in range(1,n):
        answer = i
        add = answer + 1
        while True:
            answer += add
            if answer == n:
                cnt += 1
            if answer > n:
                break
            add += 1
    return cnt