def solution(babbling):
    answer = 0
    bab = ["aya","ye","woo","ma"]
    for elements in babbling:
        for check in bab:
            if(check in elements):
                elements = elements.replace(check,"1")
        print(elements)
        if(elements.isdigit()):
                answer = answer + 1
    return answer