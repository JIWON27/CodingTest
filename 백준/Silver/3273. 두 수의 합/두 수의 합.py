n = int(input()) # 배열의 원소 개수
arr = sorted(list(map(int, input().split()))) # 배열
x = int(input()) # 비교값

cnt = 0

i, j = 0, -1
while arr[i] != arr[j]:
    if arr[i] + arr[j] == x:
        cnt += 1

    if arr[i] + arr[j] < x:
        i += 1
    else:
        j -= 1

print(cnt)

