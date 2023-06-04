from collections import Counter
def solution(my_string): 
    answer = [0 for _ in range(0,52)]
    for i in my_string: 
        if 65 <= ord(i) <= 90: 
            answer[ord(i)-65] += 1
        elif 97 <= ord(i) <= 122: 
            answer[ord(i)-71] += 1
    return answer