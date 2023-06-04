def solution(arr):
    answer = []
    start = 0
    for i in range(len(arr)):
        if arr[i] == 2:
            start = i
            break
    end = 0
    for i in range(len(arr)):
        if arr[i] == 2:
             end = i
    return [-1] if 2 not in arr else arr[start:end+1]