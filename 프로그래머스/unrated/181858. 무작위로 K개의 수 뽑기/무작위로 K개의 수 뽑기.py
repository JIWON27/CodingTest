def solution(arr, k):
    answer = []
    for value in arr:
        if value not in answer and len(answer) < k:
            answer.append(value)
    while len(answer) < k:
        answer.append(-1)
    return answer