from collections import deque
from sys import stdin

n = int(stdin.readline())
deque = deque()

for _ in range(n):
    text = stdin.readline().split()
    if text[0] == "push":
        deque.append(int(text[1]))
    elif text[0] == "pop":
        if len(deque) != 0:
            print(deque.popleft())
        else:
            print(-1)
    elif text[0] == "size":
        print(len(deque))
    elif text[0] == "empty":
        if len(deque) != 0:
            print(0)
        else:
            print(1)
    elif text[0] == "front":
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    else: # back
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)