from itertools import combinations
def solution(a, b, c, d):
    answer = 0 
    arr = [a,b,c,d]
    arr.sort()
    if len(set(arr)) == 1:
        answer = 1111 * a
    elif len(set(arr)) == 2:
        if arr[1] != arr[2]:
            answer = (arr[0]+arr[3]) * abs(arr[0]-arr[3])
        else:
            if arr[0] == arr[1]:
                answer = (10*arr[0]+arr[3])**2
            else:
                answer = (10*arr[3]+arr[0])**2
    elif len(set(arr)) == 3:
        if arr[0] == arr[1]: answer = arr[2]*arr[3]
        elif arr[1] == arr[2]: answer = arr[0]*arr[3]
        else: answer = arr[0]*arr[1]
    elif len(set(arr)) == 4:
        answer = min(arr)
    return answer