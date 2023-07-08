import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque([math.ceil((100-progress)/speed) for progress,speed in zip(progresses,speeds)])
    
    progress1 = progresses.popleft()  
    cnt = 1
    
    while progresses:
        progress2 = progresses.popleft() 
        if progress1 < progress2: 
            answer.append(cnt) 
            progress1 = progress2  
            cnt = 1
        else:
            cnt += 1 
            
        if len(progresses) == 0:
            answer.append(cnt)
            
    return answer