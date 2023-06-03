def solution(arr):
    index = 0
    while len(arr) > 2**index:
        index += 1
    for _ in range(2**index-len(arr)):
        arr.append(0)
    return arr