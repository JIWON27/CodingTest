def solution(myString, pat):
    answer = []
    for i in range(len(myString)):
        answer.append(myString[i:i+len(pat)])
    return answer.count(pat)