def solution(citations):
    answer = [0]
    n = len(citations) 
    
    for h in range(max(citations)):
        cnt_h_up = 0
        cnt_h_down = 0
        for citation in citations:
            if citation >= h:
                cnt_h_up += 1
        if cnt_h_up >= h:
            answer.append(h)   
    return max(answer)
