#연속해서 발음xx -> yeye 이런거 발음 못함
def solution(babbling):
    answer = 0   
    for elements in babbling:
        elements = elements.replace("aya","1")
        elements = elements.replace("ye","2")
        elements = elements.replace("woo","3")
        elements = elements.replace("ma","4")
        if(elements.isdigit()):
            answer += 1
            if("11" in elements):
                answer -=1
            elif("22" in elements):
                answer -=1
            elif("33" in elements):
                answer -=1
            elif("44" in elements):
                answer -=1
    return answer