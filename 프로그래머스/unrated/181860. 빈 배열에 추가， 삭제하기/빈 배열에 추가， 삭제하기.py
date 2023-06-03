def solution(arr, flag):
    answer = []
    for i,value in enumerate(flag):
        if value:
            for _ in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for _ in range(arr[i]):
                answer.pop()
    return answer