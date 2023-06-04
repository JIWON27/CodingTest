def solution(arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        answer.append([k+l for k,l in zip(i,j)])
    return answer