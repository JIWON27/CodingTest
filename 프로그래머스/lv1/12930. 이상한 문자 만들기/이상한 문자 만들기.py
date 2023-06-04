def solution(s):
    answer = ''
    index = 0
    for i in range(len(s)):
        if s[i].isalpha():
            index += 1
        else:
            index = 0
        if index % 2 == 1:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer