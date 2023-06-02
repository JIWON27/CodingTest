def solution(n):
    answer = 0
    arr = []
    for i in range(0,201):
        if (i+1) % 3 != 0 and "3" not in str(i+1):
            arr.append(i+1) 
    return arr[n-1]