def solution(number, limit, power):
    answer = []
    for i in range(number):
        answer.append(약수(i+1))
    for i,value in enumerate(answer):
        if value > limit:
            answer[i] = power
    return sum(answer)

def 약수(num) :
    cnt = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            cnt += 2
    if int(num**0.5)**2 == num:
        cnt -= 1
    return cnt