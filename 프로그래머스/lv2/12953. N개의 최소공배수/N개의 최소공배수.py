def solution(arr):
    max_num = max(arr)
    arr.sort()
    cnt = 1
    while True:
        boolean = True
        for i in range(0,len(arr)-1):
            if (max_num * cnt) % arr[i] != 0:
                boolean = False
        if boolean :
            return max_num * cnt
        cnt += 1