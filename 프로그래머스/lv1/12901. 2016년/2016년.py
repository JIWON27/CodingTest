def solution(a, b):
    answer = {0 : 'FRI', 1 : 'SAT', 2 : 'SUN', 3 : 'MON' , 4 : 'TUE', 5 :'WED' , 6 : 'THU'}
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    result = b-1
    for i in range(a-1):
        result += day[i]
    return answer[result%7]