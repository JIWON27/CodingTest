def solution(arr):
    answer = [i for i in arr]
    cnt = 0
    while True:
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i]//2
            elif arr[i] < 50 and arr[i] % 2 != 0:
                 arr[i] = arr[i]*2+1
        cnt += 1
        if answer == arr:
            break
        else:
            for i in range(len(answer)):
                answer[i] = arr[i]
    return cnt - 1