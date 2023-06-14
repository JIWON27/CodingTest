from collections import deque
def solution(s):
    s = deque(s)
    arr = deque()
    arr.append(s.popleft())
    while len(s) != 0:
        curr = s.popleft()
        if len(arr) == 0:
            arr.append(curr)
            continue
        if arr[0] == curr:
            arr.popleft()
        else:
            arr.appendleft(curr)
    return 1 if len(arr) == 0 else 0