from itertools import combinations

def solution(dots):
    answer = 0
    dots.sort(key=lambda x:x[0]) #x좌표를 기준으로 정렬
    combi = list(combinations(dots,2)) #4c2 
    for i in range(0,3):
        num1 = combi[i]
        num2 = combi[len(combi)-1-i]
        gradient1 = 0
        gradient2 = 0
        if ( (num1[1])[1]-(num1[0])[1] !=0 and (num1[1])[0]-(num1[0])[0] !=0 ):
            gradient1 = ((num1[1])[1]-(num1[0])[1]) / ((num1[1])[0]-(num1[0])[0])
        if ( (num2[1])[1]-(num2[0])[1] !=0 and (num2[1])[0]-(num2[0])[0] !=0 ):
            gradient2 = ((num2[1])[1]-(num2[0])[1]) / ((num2[1])[0]-(num2[0])[0])
        if gradient1 == gradient2:
            answer = 1
            break
    return answer