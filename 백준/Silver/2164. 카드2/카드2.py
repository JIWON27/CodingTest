from collections import deque
from sys import stdin

n = int(stdin.readline())
arr = [i+1 for i in range(n)]
deque = deque(arr)

while len(deque) != 1:
    deque.popleft()
    deque.append(deque.popleft())
print(deque[0])
