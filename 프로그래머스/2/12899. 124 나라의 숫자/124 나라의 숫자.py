def solution(n):
    answer = ''
    arr = ['4','1','2']
    while n > 0:
        if n % 3 == 0:
            n = n//3-1 # 몫에서 -1, 나머지가 0이 되면 안되니까
            answer += '4'
        else:
            answer += str(n%3)
            n = n//3
    answer.replace('3', '4')
    return answer[::-1]