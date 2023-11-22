def solution(common):
    answer = 0
    if common[1]-common[0] == common[2] - common[1]:
        answer = common[0] + (len(common) * (common[1]-common[0]))
    else:
        answer = common[len(common)-1] * (common[2]//common[1])
    return answer