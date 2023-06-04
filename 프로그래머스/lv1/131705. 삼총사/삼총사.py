from itertools import combinations

def solution(number):
    answer = list(combinations(number,3))
    cnt = 0
    for i in answer:
        if sum(i) == 0:
            cnt += 1
    return cnt