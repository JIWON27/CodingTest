def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()
    print(d)
    for i in d:
        if answer+i > budget:
            break
        answer += i
        cnt += 1
    return cnt