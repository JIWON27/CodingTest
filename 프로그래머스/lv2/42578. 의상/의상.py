def solution(clothes):
    answer = 1
    
    dict_clothes = {}
    
    for i in clothes:
        dict_clothes[i[1]] = 1
        
    for wear in clothes:
        dict_clothes[wear[1]] += 1
        
    for key, value in dict_clothes.items():
        answer *= value
    return answer - 1