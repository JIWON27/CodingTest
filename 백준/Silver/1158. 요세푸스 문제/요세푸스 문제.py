from collections import deque

n = list(map(int, input().split()))
arr = [i+1 for i in range(n[0])]
deque = deque(arr)
answer = ""

while deque:
    for _ in range(n[1]-1):
        deque.append(deque.popleft())
    answer += str(deque.popleft())+", "
print("<"+answer[0:len(answer)-2]+">")