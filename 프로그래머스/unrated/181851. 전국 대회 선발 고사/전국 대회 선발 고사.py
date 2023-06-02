def solution(rank, attendance):
    answer = []
    result = []
    for i,value in enumerate(attendance):
        if value:
            answer.append(rank[i])
    if len(answer) !=3:
        maxNum = max(answer)
        answer.remove(maxNum)
    answer.sort()
    for i in answer :
        for j in range(len(rank)):
            if i == rank[j]:
                result.append(j)
    return 10000*result[0]+100*result[1]+result[2]