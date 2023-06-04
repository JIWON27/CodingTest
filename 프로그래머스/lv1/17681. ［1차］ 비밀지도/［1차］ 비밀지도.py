def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        answer.append(format(i|j ,'b').zfill(n))
    for i in range(len(answer)):
        answer[i] = answer[i].replace(str(1),'#')
        answer[i] = answer[i].replace(str(0),' ')
    return answer