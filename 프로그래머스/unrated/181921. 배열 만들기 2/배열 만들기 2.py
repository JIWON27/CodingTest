import re
def solution(l, r):
    answer = []
    Regex = re.compile(r"^[05]+$")
    for i in range(l, r+1):
        if re.match(Regex,str(i)):
            answer.append(i)
    return [-1] if len(answer) == 0 else answer