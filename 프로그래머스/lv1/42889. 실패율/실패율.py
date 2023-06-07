from collections import Counter
def solution(N, stages):
    fail = []
    stages.sort()
    for i in range(1,N+1):
        cnt = 0
        if stages.count(i) == 0:
            fail.append(0)
        else:
            for _ in range(stages.count(i)):
                cnt += 1
                stages.pop(0)
            fail.append(cnt/(len(stages)+cnt)) 
    fail = sorted([(stage+1, value) for stage, value in enumerate(fail)], key=lambda x: x[1], reverse=True)
    return [i[0] for i in fail]