n = int(input())
stack = []
popList = []
result = []
seq = []
index = 0
cnt = 0

for _ in range(n):
    seq.append(int(input()))
    
for num in seq:
    while cnt == 0 or stack[len(stack)-1] != num:
        cnt += 1
        index += 1
        if index > n:
            break
        stack.append(index)
        result.append("+")
        
    if stack[len(stack)-1] == num:
        popList.append(stack.pop())
        result.append("-")
        cnt -= 1
    else:
        result = []
        break
if len(result) > 0:
    print(*result, sep='\n')
else:
    print("NO")