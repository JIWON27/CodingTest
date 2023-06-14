def solution(answers):
    score = [0,0,0]
    num1 = [1,2,3,4,5] 
    num2 = [2,1,2,3,2,4,2,5] 
    num3 = [3,3,1,1,2,2,4,4,5,5] 
    
    for i,value in enumerate(answers):
        if num1[i%5] == value:
            score[0] += 1   
        if num2[i%8] == value:
            score[1] += 1   
        if num3[i%10] == value:
            score[2] += 1
            
    if len(set(score)) == 1:
        return [1,2,3]
    else:
        result = []
        for i in range(len(score)):
            if max(score) == score[i]:
                result.append(i+1)
    return result