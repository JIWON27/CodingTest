def solution(cards1, cards2, goal):
    answer = 'Yes'
    check1 = []
    check2 = []
    for i in goal:
        if i in cards1:
            check1.append(i)
        elif i in cards2:
            check2.append(i)
    for i, j in zip(check1, cards1):
        if i != j:
            answer = 'No'
            break
        else:
            for i, j in zip(check2, cards2):
                if i != j:
                    answer = 'No'
                    break
    return answer