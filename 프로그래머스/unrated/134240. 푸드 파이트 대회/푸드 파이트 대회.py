def solution(food):
    answer = ''
    for i,value in enumerate(food):
        if value != 1:
            answer = answer[0:len(answer)//2]+str(i) * (value//2) * 2+answer[len(answer)//2:]
    return answer[0:len(answer)//2]+str(0)+answer[len(answer)//2:]