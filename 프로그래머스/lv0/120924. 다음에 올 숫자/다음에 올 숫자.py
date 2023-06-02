def solution(common):
    #등차 : an = a + (n-1)d
    #등비 : an = a * r ^ (n-1)
    answer = 0
    if common[1]-common[0] == common[2] - common[1]:
        answer = common[0] + (len(common) * (common[1]-common[0]))
    else:
        answer = common[len(common)-1] * (common[2]//common[1])
    return answer