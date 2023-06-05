from itertools import combinations
def solution(nums):
    answer = 0
    num = [sum(i)for i in list(combinations(nums,3))]
    for i in num:
        if prime(i) == 2:
            answer += 1
    return answer

def prime(num):
    cnt = 2
    for i in range(2, num):
        if num % i == 0:
            cnt += 1
    return cnt