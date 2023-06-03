import re
def solution(myStr):
    Regex = re.compile('[^abc]+')
    answer = re.findall(Regex, myStr)
    return ["EMPTY"] if len(answer) == 0 else answer