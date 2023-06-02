import re
def solution(dartResult):
    score = []
    dartReg = re.compile('[0-9]+[SDT][*#]?')
    tokens = re.findall(dartReg, dartResult)
    for index,value in enumerate(tokens):
        num = 0
        if 'S' in value : 
            num = int(re.sub(r'\D', '', value))**1
        elif 'D' in value: 
            num = int(re.sub(r'\D', '', value))**2
        else: 
            num = int(re.sub(r'\D', '', value))**3
        if '*' in value:
            num = num * 2
            if index > 0:
                score[index-1] = score[index-1]*2
        elif '#' in value: 
            num = num * (-1)
        score.append(num)
    return sum(score)