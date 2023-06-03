def solution(s):
    answer = []
    for i in s.split(" "):
        answer.append(int(i))
    answer.sort()
    return  str(answer[0])+' '+str(answer[len(answer)-1])