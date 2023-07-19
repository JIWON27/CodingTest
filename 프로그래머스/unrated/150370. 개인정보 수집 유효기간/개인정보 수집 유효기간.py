def solution(today, terms, privacies):
    answer = []
    term = {i[0] : i[2:] for i in terms}
    
    today = today.split(".")
    
    for idx, privacy in enumerate(privacies):
        day = privacy.split(" ")
        date = day[0].split(".")
        
        expiry =  int(date[1]) + int(term.get(day[1]))
            
        newTodayYear = date[0]
        newTodayMonth = ( int(today[0]) - int(date[0]) ) * 12 + int(today[1])
        
        if newTodayMonth > expiry:
            answer.append(idx+1) 
        elif newTodayMonth == expiry:
            if int(today[2]) >= int(date[2]):
                answer.append(idx+1) 
    return answer