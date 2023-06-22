n = input()
answer = 1
for i in range(1, int(n)+1):
    answer *= i
cnt = 0
for num in str(answer)[::-1]:
    if num != '0':
        break
    else:
        cnt += 1
print(cnt)
    
