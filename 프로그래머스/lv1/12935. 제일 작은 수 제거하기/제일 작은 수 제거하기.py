def solution(arr):
    minNum = min(arr)
    arr.remove(minNum)
    if len(arr) == 0:
        arr.append(-1)
    return arr