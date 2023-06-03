def solution(myString, pat):
    index = 0
    for i in range(len(myString)):
        if myString[i:i+len(pat)] == pat:
            index = i
    return myString[:index+len(pat)]