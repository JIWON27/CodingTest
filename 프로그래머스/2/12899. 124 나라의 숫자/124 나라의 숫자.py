def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 0:
            n = n//3-1 
            answer += '4'
        else:
            answer += str(n%3)
            n = n//3
    answer.replace('3', '4')
    return answer[::-1]