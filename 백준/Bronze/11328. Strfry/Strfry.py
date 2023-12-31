n = int(input()) # 배열의 원소 개수

for i in range(n):
    arr = list(input().split())  # 배열
    for j in arr[0]:
        if j in arr[1]:
            arr[1] = arr[1].replace(j, "-", 1) # arr[1] 대입 안해도 되는줄 알았음.
    
    if arr[1].count("-") == len(arr[1]) and len(arr[0]) == len(arr[1]):
        print("Possible")
    else:
        print("Impossible")