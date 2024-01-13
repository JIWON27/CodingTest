def solution(n, words):
    check = [] # 앞에 나온 단어인지 아닌지 확인용 배열
    
    check.append(words[0])
    for i in range(1,len(words)):
        if words[i] not in check and check[-1][-1] == words[i][0]:
            check.append(words[i])
        else:
            return [i%n+1, len(check)//n+1]
    return [0,0]
            
            
        
            
        
        
    
    
            